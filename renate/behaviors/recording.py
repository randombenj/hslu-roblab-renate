import time
import logging
import tempfile
import os.path as path
import librosa



from renate.utils import (
    track_beat,
    download_file_from_pepper,
    upload_file_to_pepper
)

RECORDING_PATH = "/home/nao/recording.wav"


def __record_audio(renate):
    logging.info("recording audio to: '{}'".format(RECORDING_PATH))
    renate.robot.ALAudioRecorder.startMicrophonesRecording(
        RECORDING_PATH,
        "wav",
        48000,
        [True, True, True, True]
    )
    time.sleep(10)
    renate.robot.ALAudioRecorder.stopMicrophonesRecording()

def __process_audio(renate):
    tmp = path.join(tempfile.mkdtemp(), "recording.wav").strip()
    logging.info("saving audio to: '{}'".format(tmp))
    download_file_from_pepper(
        renate.robot.configuration,
        RECORDING_PATH,
        tmp
    )
    tempo, beats, y, sr = track_beat(tmp)
    logging.info("got beat '{}', tracking '{}'".format(tempo, beats))
    upload_file_to_pepper(
        renate.robot.configuration,
        tmp,
        RECORDING_PATH
    )

def recording(renate):
    say = "Give me some music!"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)

    __record_audio(renate)

    say = "Okay, I thik that's quite enough! Thinking about good dancemoves now!"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)

    __process_audio(renate)

