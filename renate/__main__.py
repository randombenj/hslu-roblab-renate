# -*- coding: utf-8 -*-

import logging

from pynaoqi_mate import Robot
from configuration import PepperConfiguration

from renate.utils import download_file_from_pepper
from renate.core import RENATE

# configure logging
logging.basicConfig(level=logging.INFO)

#: Holds the name of the Pepper
PEPPER_NAME = "Amber"


def main():
    config = PepperConfiguration(PEPPER_NAME)
    robot = Robot(config)

    renate = RENATE(robot)
    renate.do_wakeup()
    renate.do_listen()
    renate.do_dance()
    #renate.do_rest()


if __name__ == "__main__":
    main()
