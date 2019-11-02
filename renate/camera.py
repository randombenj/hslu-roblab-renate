import os
import uuid
import logging

from .utils import download_file_from_pepper


REMOTE_TEMP_FOLDER = "/home/nao/recordings/cameras/"


class Camera(object):
    def __init__(self, robot):
        self.robot = robot
        self.camera = robot.ALPhotoCapture

    def take_picture(self, local_path, resolution=4):
        self.camera.setResolution(resolution)
        self.camera.setColorSpace(0)
        remote_temp_filename = str(uuid.uuid4()) + ".jpg"
        remote_temp_path = os.path.join(
                REMOTE_TEMP_FOLDER,
                remote_temp_filename
        )
        logging.info("Taking picture ...")
        self.camera.takePicture(REMOTE_TEMP_FOLDER, remote_temp_filename)
        logging.info("Took picture and stored to %s", os.path.join(remote_temp_path))
        logging.info("Downloading picture to %s", local_path)
        download_file_from_pepper(
                self.robot.configuration, remote_temp_path, local_path)
        logging.info("Downloaded picture to %s", local_path)
