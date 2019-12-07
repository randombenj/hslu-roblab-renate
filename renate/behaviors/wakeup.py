import logging


def wakeup(renate):
    if not renate.robot.ALMotion.robotIsWakeUp():
        say = "Holy Moly was I asleep!"
        logging.info(say)
        renate.robot.ALAnimatedSpeech.say(say)
        renate.robot.ALMotion.wakeUp()

    renate.robot.ALAutonomousLife.setState('interactive')
    renate.robot.ALRobotPosture.goToPosture("StandInit", 1.0)
    # do voice stuff
    renate.robot.ALTextToSpeech.setParameter("doubleVoice", 1)
    renate.robot.ALTextToSpeech.setParameter("doubleVoiceLevel", 0.5)
    renate.robot.ALTextToSpeech.setParameter("doubleVoiceTimeShift", 0.1)
    renate.robot.ALTextToSpeech.setParameter("pitchShift", 1.1)
    #renate.robot.ALTextToSpeech.setVoice("Kenny22Enhanced")
    renate.robot.ALTextToSpeech.say("fuck!")
