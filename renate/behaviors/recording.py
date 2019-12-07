import time
import logging
import tempfile
import os.path as path
import librosa



from renate.utils import (
    track_beat,
    track_accurate_beat,
    download_file_from_pepper,
    upload_file_to_pepper
)

RECORDING_PATH = "/home/nao/recording.wav"


def __record_audio(renate):
    logging.info("recording audio to: '{}'".format(RECORDING_PATH))
    renate.robot.ALAudioRecorder.stopMicrophonesRecording()
    renate.robot.ALAudioRecorder.startMicrophonesRecording(
        RECORDING_PATH,
        "wav",
        48000,
        [True, True, True, True]
    )
    time.sleep(30)
    renate.robot.ALAudioRecorder.stopMicrophonesRecording()

def __process_audio(renate):
    tmp = path.join(tempfile.mkdtemp(), "recording.wav").strip()
    logging.info("saving audio to: '{}'".format(tmp))
    download_file_from_pepper(
        renate.robot.configuration,
        RECORDING_PATH,
        tmp
    )
    renate.robot.ALAnimatedSpeech.say("Thinking about good dancemoves now!")
    #tempo, beats, y, sr = track_beat(tmp)
    beats, y, sr = track_accurate_beat(tmp)
    logging.info("got tracking '{}'".format(beats))
    renate.robot.ALAnimatedSpeech.say("Nearly done, beep beep boop!")
    renate.beats = beats
    upload_file_to_pepper(
        renate.robot.configuration,
        tmp,
        RECORDING_PATH
    )

def recording(renate):
    say = "Give me some music, then I can show you sick moves!"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)

    __record_audio(renate)

    say = "Okay, I thik that's quite enough!"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)

    __process_audio(renate)

