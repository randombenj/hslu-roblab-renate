import sys
import logging

from transitions.extensions import GraphMachine as Machine

from renate.tablet_service import TabletService

from renate.behaviors.resting import resting
from renate.behaviors.wakeup import wakeup
from renate.behaviors.dancing import dancing
from renate.behaviors.recording import recording
from renate.behaviors.follow import start_following, stop_following

# school room orientations
SCHOOL_ON_HIS_RIGHT = -1
SCHOOL_ON_HIS_LEFT = 1


class RENATE(object):
    STATES = [
        "start",
        "wakeup",
        "start_following",
        "stop_following",
        "recording",
        "dancing",
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
                trigger="do_start_follow",
                source=["wakeup", "recording", "dancing"],
                dest="start_following",
                after=lambda *args, **kwargs: start_following(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="do_stop_follow",
                source=["start_following", "dancing"],
                dest="stop_following",
                after=lambda *args, **kwargs: stop_following(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="do_listen",
                source=["wakeup", "start_following"],
                dest="recording",
                after=lambda *args, **kwargs: recording(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="do_dance",
                source=["recording", "wakeup", "start_following"],
                dest="dancing",
                after=lambda *args, **kwargs: dancing(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="do_rest",
                source=["dancing", "following", "stop_following"],
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

    def move(self, x, y):
        # return self.robot.ALNavigation.navigateTo(x, y)
        self.robot.ALMotion.moveTo(x, y, 0)
        return True


if __name__ == "__main__":
    # Generate FSM graph
    renate = RENATE(None)
    renate.state_machine.get_graph().draw(sys.argv[1], prog="dot")
