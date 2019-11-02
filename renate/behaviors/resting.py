import logging


def resting(renate):
    say = "I'm so tired, I'm going to rest"
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)
    renate.robot.ALMotion.rest()
