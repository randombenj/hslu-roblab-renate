import time
import logging


def recording(renate):
    say = "Give me some music!"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)
    path = "/home/nao/recording.wav"
    logging.info("recording audio to: '{}'".format(path))
    renate.robot.ALAudioRecorder.startMicrophonesRecording(
        path,
        "wav",
        48000,
        [True, True, True, True]
    )
    time.sleep(10)
    renate.robot.ALAudioRecorder.stopMicrophonesRecording()
    say = "Okay, I thik that's quite enough!"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)