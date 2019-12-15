import sys
import time
import threading
import logging

from transitions.extensions import GraphMachine as Machine

from renate.tablet_service import TabletService

from renate.behaviors.resting import resting
from renate.behaviors.wakeup import wakeup
from renate.behaviors.dancing import dancing
from renate.behaviors.recording import recording
from renate.behaviors.dialog import dialog

# school room orientations
SCHOOL_ON_HIS_RIGHT = -1
SCHOOL_ON_HIS_LEFT = 1


class RENATE(object):
    STATES = [
        "start",
        "wakeup",
        "recording",
        "dancing",
        "dialog",
        "resting",
        "error"
    ]

    def __init__(self, robot):
        self.robot = robot
        self.following = False
        self.beats = []

        self.tablet = robot.session.service("ALTabletService")

        self.state_machine = Machine(model=self, states=self.STATES, queued=True, initial="start")
        self.state_machine.add_transition(
            trigger="do_wakeup",
            source=["start", "resting"],
            dest="wakeup",
            after=lambda *args, **kwargs: wakeup(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="do_listen",
            source=["wakeup", "dialog"],
            dest="recording",
            after=lambda *args, **kwargs: recording(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="do_dance",
            source=["recording", "dialog"],
            dest="dancing",
            after=lambda *args, **kwargs: dancing(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="do_dialog",
            source=["dancing", "start"],
            dest="dialog",
            after=lambda *args, **kwargs: dialog(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="do_rest",
            source=["dialog"],
            dest="resting",
            after=lambda *args, **kwargs: resting(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="do_fail",
            source=self.STATES,
            dest="error",
            after=self.__on_error
        )

    def __on_error(self, reason):
        logging.error("Got into Error state becase: '%s'", reason)
        self.robot.ALAnimatedSpeech.say("Error! Error!")
        self.robot.ALAnimatedSpeech.say("I'm confusion and don't know what to do")
        self.robot.ALAnimatedSpeech.say("I think the reason is that {}".format(reason))

    def start_following(self):
        def follow(renate):
            """follow"""
            desired_range = 0.6
            threshhold = (-0.05, 0.05)
            while renate.following:
                time.sleep(0.2)
                sonar_front = renate.robot.ALMemory.getData(
                    "Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
                logging.info("Got sonar value of: %f", sonar_front)
                if sonar_front > 1.2:
                    logging.info("no object in front")
                    continue

                distance = sonar_front - desired_range
                logging.info("distance to target: %s", distance)

                if distance < threshhold[0] or distance > threshhold[1]:
                    # move toward dancer
                    logging.info("moving to target")
                    renate.move(distance, 0)

        self.following = True
        thread = threading.Thread(target=follow, args=[self])
        thread.daemon = True
        thread.start()

    def stop_following(self):
        self.following = False

    def move(self, x, y):
        self.robot.ALMotion.moveTo(x, y, 0)
        return True


if __name__ == "__main__":
    # Generate FSM graph
    renate = RENATE(None)
    renate.state_machine.get_graph().draw(sys.argv[1], prog="dot")
