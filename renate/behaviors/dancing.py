import time
import threading
import logging
import numpy as np

import qi


def calculate_dancemoves(beats):
    data = beats
    dist = np.array([j-i for i, j in zip(data[:-1], data[1:])])

    half_time = False
    mean = dist.mean()
    logging.info("mean: %s, this is %s bpm", mean, 1/mean*60)
    if mean <= 0.50:
        half_time = True
        data2 = list()
        for idx, v in enumerate(data):
            if idx == 0:
                continue
            if idx % 2 == 0:
                data2.append(v) #) + data[idx-1])
        #del data2[::2]
        data = data2
    logging.info("got data %s", data)
    return data, half_time


def dancing(renate):
    time.sleep(1)
    names = []
    times = []
    keys = []

    names.append("HeadPitch")
    times.append([0.96, 2.36, 3.16, 3.96])
    keys.append([[0.233874, [3, -0.333333, 0], [3, 0.466667, 0]], [-0.38182, [3, -0.466667, 0], [3, 0.266667, 0]],
                 [-0.38182, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.38182, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([2.36, 3.16, 3.96])
    keys.append([[0.0126637, [3, -0.8, 0], [3, 0.266667, 0]], [0.0126637, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.0126637, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("HipPitch")
    times.append([0, 0.76, 0.96, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[-0.235619, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.235619, [3, -0.253333, 0], [3, 0.0666667, 0]],
                 [-0.459022, [3, -0.0666667, 0], [3, 0.2, 0]],
                 [-0.235619, [3, -0.2, -0.0573465], [3, 0.266667, 0.0764621]],
                 [-0.0575959, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.185005, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.0488692, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.235619, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("HipRoll")
    times.append([0, 0.76, 0.96, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[-0.20944, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.253073, [3, -0.253333, 0], [3, 0.0666667, 0]],
                 [-0.00698132, [3, -0.0666667, 0.0385427], [3, 0.2, -0.115628]],
                 [-0.20944, [3, -0.2, 0], [3, 0.266667, 0]], [0.202458, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.268781, [3, -0.266667, 0], [3, 0.266667, 0]], [0.202458, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.20944, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("KneePitch")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.0488692, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.0488692, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [0.0488692, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.514872, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.0122173, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0128281, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.0488692, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[-0.699877, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.00872665, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [-0.699877, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-1.06116, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.112096, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.699877, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[-0.420624, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.34383, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [-0.420624, [3, -0.266667, 0.260054], [3, 0.266667, -0.260054]],
                 [-1.21649, [3, -0.266667, 0], [3, 0.266667, 0]], [0.191986, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-1.71858, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.420624, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.02, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.02, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [0.02, [3, -0.266667, 0], [3, 0.266667, 0]], [0.02, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.02, [3, -0.266667, 0], [3, 0.266667, 0]], [0.02, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.02, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[1.03149, [3, -0.0133333, 0], [3, 0.253333, 0]], [1.41023, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [1.03149, [3, -0.266667, 0], [3, 0.266667, 0]], [1.93732, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [1.69297, [3, -0.266667, 0.20304], [3, 0.266667, -0.20304]],
                 [0.719076, [3, -0.266667, 0], [3, 0.266667, 0]], [1.03149, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.00872665, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.179769, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]], [1.13446, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]], [0.938987, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.00872665, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.815069, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.666716, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [0.815069, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.651008, [3, -0.266667, 0.115774], [3, 0.266667, -0.115774]],
                 [0.120428, [3, -0.266667, 0], [3, 0.266667, 0]], [1.82387, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.815069, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.00872665, [3, -0.0133333, 0], [3, 0.253333, 0]], [1.2514, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]], [0.891863, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]], [0.891863, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.00872665, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.914553, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.392699, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [0.914553, [3, -0.266667, 0], [3, 0.266667, 0]], [0.595157, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [2.08567, [3, -0.266667, 0], [3, 0.266667, 0]], [0.595157, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.914553, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0, 0.76, 0.96, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[0.02, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.02, [3, -0.253333, 0], [3, 0.0666667, 0]],
                 [0.64, [3, -0.0666667, 0], [3, 0.2, 0]], [0.02, [3, -0.2, 0], [3, 0.266667, 0]],
                 [0.02, [3, -0.266667, 0], [3, 0.266667, 0]], [0.02, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [0.02, [3, -0.266667, 0], [3, 0.266667, 0]], [0.02, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[1.11352, [3, -0.0133333, 0], [3, 0.253333, 0]], [2.08567, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [1.11352, [3, -0.266667, 0.109956], [3, 0.266667, -0.109956]],
                 [1.00356, [3, -0.266667, 0], [3, 0.266667, 0]], [1.30376, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [1.00356, [3, -0.266667, 0], [3, 0.266667, 0]], [1.11352, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[-1.18159, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.251327, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [-1.18159, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.191986, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00872665, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-1.18159, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0, 0.76, 1.56, 2.36, 3.16, 3.96, 4.76])
    keys.append([[-0.781907, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.781907, [3, -0.253333, 0], [3, 0.266667, 0]],
                 [-0.781907, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0374316, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-1.82387, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0374316, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.781907, [3, -0.266667, 0], [3, 0, 0]]])

    data, half_time = calculate_dancemoves(renate.beats)
    try:
        renate.robot.ALAudioPlayer.setMasterVolume(1.0)
        sound_future = qi.async(renate.robot.ALAudioPlayer.playFile, "/home/nao/recording.wav")
        renate.start_following()
        repetition = int(len(data) / 8)
        for i in range(repetition):
            start_index = i * 8
            new_times = list()
            for t in times:
                newt = data[start_index:(start_index+len(t))]
                newt = [float(x - newt[0]) for x in newt]
                new_times.append(newt)

            renate.robot.ALMotion.angleInterpolationBezier(names, new_times, keys)
        renate.stop_following()
        renate.robot.ALAudioPlayer.stopAll()
    except Exception as exc:
        fail_reason = "Unable to dance, because: '{}'".format(exc)
        logging.error(fail_reason)
        renate.do_fail(reason=fail_reason)

    renate.do_stop_follow()