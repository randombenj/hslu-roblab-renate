# -*- coding: utf-8 -*-

import time
import logging
import argparse

from pynaoqi_mate import Robot
from configuration import PepperConfiguration

from renate.utils import download_file_from_pepper
from renate.core import RENATE

# configure logging
logging.basicConfig(level=logging.INFO)

#: Holds the name of the Pepper
PEPPER_NAME = "Porter"

def main(pepper_name):
    config = PepperConfiguration(pepper_name)
    robot = Robot(config)

    renate = RENATE(robot)

    renate.do_wakeup()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pepper_name", nargs='?', default="Amber", choices=['Amber', 'Porter', 'Pale'])

    main(parser.parse_args().pepper_name)
