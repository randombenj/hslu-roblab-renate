# -*- coding: utf-8 -*-

import logging

from pynaoqi_mate import Robot
from configuration import PepperConfiguration

from renate.core import RENATE

# configure logging
logging.basicConfig(level=logging.INFO)

#: Holds the name of the Pepper
PEPPER_NAME = "Amber"


def main():
    config = PepperConfiguration(PEPPER_NAME)
    robot = Robot(config)

    renate = RENATE(robot)
    renate.wakeup()
    renate.do_dance()
    renate.rest()


if __name__ == "__main__":
    main()
