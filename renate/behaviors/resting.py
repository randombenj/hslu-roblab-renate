import logging


def resting(renate):
    say = "This was an exhausting dance lesson! I am very tired, I'm going to rest a bit."
    logging.info(say)
    renate.robot.ALAnimatedSpeech.say(say)
    renate.robot.ALMotion.rest()
