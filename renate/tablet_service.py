#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import os
import shutil
import qi


class TabletService:
    LOCAL_PATH = "/opt/aldebaran/var/www/apps/"
    LOCAL_URL = "http://198.18.0.1/apps/"

    def __init__(self, app_name, session):
        self.__tablet_service = session.service("ALTabletService")
        self.__app_name = app_name
        self.__app_folder_path = os.path.join(TabletService.LOCAL_PATH, self.__app_name)
        self.__initialize_directories(self.__app_folder_path)
        self.__callback_id_dict = dict()
        self.__dialog_promise = None
        self.__dialog_signal_id = self.__dialog_register()
        self.reinit_tablet()

    def reinit_tablet(self):
        try:
            self.__tablet_service.resetTablet()
            if self.get_wifi_status() != 'CONNECTED':
                self.__initialize_wifi()
        except Exception as e:
            print 'Error was: {}'.format(e)

    def __initialize_wifi(self):
        try:
            self.__tablet_service.enableWifi()
            self.__tablet_service.configureWifi('wpa', 'alexahslu', 'alexahslu1234')
            self.__tablet_service.connectWifi('alexahslu')
        except Exception as e:
            print 'Error was: {}'.format(e)

    def get_wifi_status(self):
        return self.__tablet_service.getWifiStatus()

    def set_volume(self, new_volume):
        self.__tablet_service.setVolume(new_volume)

    def build_local_path(self, relative_path):
        return os.path.join(self.__app_folder_path, relative_path)

    def build_local_url(self, relative_url):
        return TabletService.LOCAL_URL + self.__app_name + "/" + relative_url

    def __initialize_directories(self, app_folder_path):
        if not os.path.exists(app_folder_path):
            os.mkdir(app_folder_path)
        if not os.path.exists(os.path.join(app_folder_path, "html")):
            os.mkdir(os.path.join(app_folder_path, "html"))
        if not os.path.exists(os.path.join(app_folder_path, "html", "tmp_files")):
            os.mkdir(os.path.join(app_folder_path, "html", "tmp_files"))

    def __remove_directories(self, app_folder_path):
        shutil.rmtree(app_folder_path)

    def transfer_folder(self, source_path, target_rel_path):
        shutil.copytree(source_path, os.path.join(self.__app_folder_path, target_rel_path))

    def transfer_file(self, source_path, filename, target_rel_path=""):
        shutil.copyfile(os.path.join(source_path, filename),
                        os.path.join(self.__app_folder_path, target_rel_path, filename))

    def close(self):
        self.__remove_directories(self.__app_folder_path)
        self.touch_disconnect_all_callbacks()
        self.__dialog_unregister(self.__dialog_signal_id)
        self.__tablet_service.resetTablet()

    ###############################
    # VIDEO                       #
    ###############################

    def video_play_local(self, video_path, file_name, transfer_needed=False):
        if transfer_needed:
            self.transfer_file(video_path, file_name, "html/tmp_files")
            self.__tablet_service.playVideo(self.build_local_url("tmp_files/" + file_name))
        else:
            self.__tablet_service.playVideo(self.build_local_url(video_path + file_name))

    def video_play_url(self, video_url):
        self.__tablet_service.playVideo(video_url)

    def video_get_video_position(self):
        return self.__tablet_service.getVideoPosition()

    def video_get_video_length(self):
        return self.__tablet_service.getVideoLength()

    def video_pause(self):
        self.__tablet_service.pauseVideo()

    def video_resume(self):
        self.__tablet_service.resumeVideo()

    def video_stop(self):
        self.__tablet_service.stopVideo()

    ###############################
    # WEBVIEW                     #
    ###############################

    def webview_show(self, url=None, local=False):
        if url is None:
            self.__tablet_service.showWebview()
        else:
            if local:
                self.__tablet_service.showWebview(self.build_local_url(url))
            else:
                self.__tablet_service.showWebview(url)

    def webview_execute_js(self, js_script):
        self.__tablet_service.executeJS(js_script)

    def webview_refresh_page(self, no_cache=True):
        self.__tablet_service.reloadPage(no_cache)

    def webview_hide(self):
        self.__tablet_service.hideWebview()

    ###############################
    # IMAGE                       #
    ###############################

    def image_show_local(self, img_path, file_name, transfer_needed=False):
        if transfer_needed:
            self.transfer_file(img_path, file_name, "html/tmp_files")
            self.__tablet_service.showImageNoCache(self.build_local_url("tmp_files/" + file_name))
        else:
            self.__tablet_service.showImageNoCache(self.build_local_url(img_path + file_name))

    def image_show_url(self, img_url):
        self.__tablet_service.showImageNoCache(img_url)

    def image_background_color(self, hex_color):
        """
        Changes the background color while displaying an image.
        :param hex_color: Format must be "#000000"
        """
        self.__tablet_service.setBackgroundColor(hex_color)

    def image_pause_gif(self):
        self.__tablet_service.pauseGif()

    def image_resume_gif(self):
        self.__tablet_service.resumeGif()

    def image_hide(self):
        self.__tablet_service.hideImage()

    ###############################
    # DIALOG                      #
    ###############################

    def dialog_show_input(self, input_type, title, ok, cancel, value=None, limit=None):
        self.__dialog_reinit_promise()

        if value is not None and limit is not None:
            self.__tablet_service.showInputDialog(input_type, title, ok, cancel, value, limit)
        else:
            self.__tablet_service.showInputDialog(input_type, title, ok, cancel)

    def dialog_show_text_input(self, title, ok, cancel, value=None, limit=None):
        self.__dialog_reinit_promise()

        if value is not None and limit is not None:
            self.__tablet_service.showInputTextDialog(title, ok, cancel, value, limit)
        else:
            self.__tablet_service.showInputTextDialog(title, ok, cancel)

    def dialog_get_result(self, timeout=qi.FutureTimeout.Infinite):
        return self.__dialog_promise.future().value(timeout)

    def dialog_hide(self):
        self.__tablet_service.hideDialog()

    def __dialog_reinit_promise(self):
        if self.__dialog_promise is not None and not self.__dialog_promise.future().isFinished():
            self.__dialog_promise.setCanceled()
        self.__dialog_promise = qi.Promise()

    def __dialog_register(self):
        return self.__tablet_service.onInputText.connect(self.__dialog_callback)

    def __dialog_unregister(self, signal_id):
        self.__tablet_service.onInputText.disconnect(signal_id)

    def __dialog_callback(self, validation, input_string):
        if self.__dialog_promise is not None and not self.__dialog_promise.future().isFinished():
            self.__dialog_promise.setValue((validation, input_string))

    ###############################
    # TOUCH                       #
    ###############################

    def touch_register_tablet_events(self, callback):
        def touchdown_callback(x, y):
            callback('touchdown', x, y)

        def touchdown_ratio_callback(x, y, view_touched):
            callback('touchdown_ratio', x, y, view_touched)

        def touchmove_callback(x, y):
            callback('touchmove', x, y)

        def touchup_callback(x, y):
            callback('touchup', x, y)

        signal_id_touchdown = self.__tablet_service.onTouchDown.connect(touchdown_callback)
        signal_id_touchdown_ratio = self.__tablet_service.onTouchDownRatio.connect(touchdown_ratio_callback)
        signal_id_touchmove = self.__tablet_service.onTouchMove.connect(touchmove_callback)
        signal_id_touchup = self.__tablet_service.onTouchUp.connect(touchup_callback)

        callback_id = len(self.__callback_id_dict)
        self.__callback_id_dict[callback_id] = (signal_id_touchdown, signal_id_touchdown_ratio,
                                                signal_id_touchmove, signal_id_touchup)

        return callback_id

    def touch_disconnect_callback(self, callback_id):
        sig_ids = self.__callback_id_dict[callback_id]
        self.__tablet_service.onTouchDown.disconnect(sig_ids[0])
        self.__tablet_service.onTouchDownRatio.disconnect(sig_ids[1])
        self.__tablet_service.onTouchMove.disconnect(sig_ids[2])
        self.__tablet_service.onTouchUp.disconnect(sig_ids[3])
        self.__callback_id_dict.pop(callback_id)

    def touch_disconnect_all_callbacks(self):
        while len(self.__callback_id_dict) > 0:
            self.touch_disconnect_callback(list(self.__callback_id_dict.keys())[0])
