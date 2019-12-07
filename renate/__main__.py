# -*- coding: utf-8 -*-

import logging
import argparse

from pynaoqi_mate import Robot
from configuration import PepperConfiguration

from renate.utils import download_file_from_pepper
from renate.core import RENATE

# configure logging
logging.basicConfig(level=logging.INFO)


def main(pepper_name):
    config = PepperConfiguration(pepper_name)
    robot = Robot(config)

    renate = RENATE(robot)
    renate.do_wakeup()
    renate.do_start_follow()
    renate.do_stop_follow()
    #renate.do_listen()
    #renate.do_dance()
    #renate.do_rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pepper_name", nargs='?', default="Amber", choices=['Amber', 'Porter'])

    main(parser.parse_args().pepper_name)
