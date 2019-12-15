import logging


def wakeup(renate):
    if not "disabled" in renate.robot.ALAutonomousLife.getState():
        renate.robot.ALAutonomousLife.setState('disabled')

    if not renate.robot.ALMotion.robotIsWakeUp():
        say = "Holy Moly was I asleep!"
        logging.info(say)
        renate.robot.ALAnimatedSpeech.say(say)
        renate.robot.ALMotion.wakeUp()
    else:
        logging.info("I'm soo awake and ready")

    # reset robot
    renate.robot.ALTracker.stopTracker()
    renate.robot.ALTracker.unregisterAllTargets()
    renate.robot.ALMotion.stiffnessInterpolation("Body", 1, 0.1)

    renate.robot.ALLeds.reset("FaceLeds")

    # do voice stuff
    renate.robot.ALTextToSpeech.setLanguage("English")
    renate.robot.ALTextToSpeech.setVolume(1.0)
    renate.robot.ALTextToSpeech.setParameter("doubleVoice", 0)
    renate.robot.ALTextToSpeech.setParameter("doubleVoiceLevel", 0.5)
    renate.robot.ALTextToSpeech.setParameter("doubleVoiceTimeShift", 0.1)
    renate.robot.ALTextToSpeech.setParameter("pitchShift", 0.7)

    # init robot
    renate.robot.ALRobotPosture.goToPosture("Stand", 1.0)
    renate.robot.ALAnimatedSpeech.say("Hello I am Renate and I am your freestile dance teacher!")