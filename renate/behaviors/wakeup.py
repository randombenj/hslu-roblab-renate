import logging


def wakeup(renate):
    if not renate.robot.ALMotion.robotIsWakeUp():
        say = "Holy Moly was I asleep!"
        logging.info(say)
        renate.robot.ALAnimatedSpeech.say(say)
        renate.robot.ALMotion.wakeUp()
        renate.robot.ALAutonomousLife.setState('interactive')
        renate.robot.ALRobotPosture.goToPosture("StandInit", 1.0)
