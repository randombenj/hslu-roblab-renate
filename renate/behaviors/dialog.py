import time
import logging

from renate.dialog import Dialog

def dialog(renate):
    speech_dialog = Dialog(renate.robot)

    topic_name = speech_dialog.load_yes_no_question("Do you want me to repeat the dance?", "Okay", "Well then")
    do_repeat = speech_dialog.ask_yes_no_question(topic_name) == "1"
    speech_dialog.stop_topic(topic_name)
    speech_dialog.close_session()

    logging.info("repeat %s", do_repeat)
    if do_repeat:
        renate.do_dance()
        return

    topic_name = speech_dialog.load_yes_no_question("Do you want me to dance to something else?", "Okay", "Well then")
    do_new = speech_dialog.ask_yes_no_question(topic_name) == "1"
    speech_dialog.stop_topic(topic_name)
    speech_dialog.close_session()

    logging.info("new recording %s", do_new)
    if do_new:
        renate.do_listen()
        return


    renate.do_rest()