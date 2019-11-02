import sys
import logging

from transitions.extensions import GraphMachine as Machine

from renate.behaviors.resting import resting
from renate.behaviors.wakeup import wakeup
from renate.behaviors.dancing import dancing

# school room orientations
SCHOOL_ON_HIS_RIGHT = -1
SCHOOL_ON_HIS_LEFT = 1


class RENATE(object):
    STATES = [
        "start",
        "wakeup",
        "dancing",
        "resting",
        "error"
    ]

    def __init__(self, robot):
        self.robot = robot

        self.state_machine = Machine(model=self, states=self.STATES, queued=True, initial="start")
        self.state_machine.add_transition(
                trigger="wakeup",
                source=["start", "resting"],
                dest="wakeup",
                after=lambda *args, **kwargs: wakeup(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="do_dance",
                source="wakeup",
                dest="dancing",
                after=lambda *args, **kwargs: dancing(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="rest",
                source="dancing",
                dest="resting",
                after=lambda *args, **kwargs: resting(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="fail",
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
