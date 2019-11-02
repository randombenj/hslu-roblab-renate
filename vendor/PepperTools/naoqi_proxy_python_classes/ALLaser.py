#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/allaserproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALLaser(object):
    def __init__(self, session):
        self.proxy = None 
        self.session = session

    def force_connect(self):
        self.proxy = self.session.service("ALLaser")

    def laserOFF(self):
        """Disable laser light
        """
        if not self.proxy:
            self.proxy = self.session.service("ALLaser")
        return self.proxy.laserOFF()

    def laserON(self):
        """Enable laser light and sampling
        """
        if not self.proxy:
            self.proxy = self.session.service("ALLaser")
        return self.proxy.laserON()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALLaser")
        return self.proxy.ping()

    def setDetectingLength(self, length_min_l, length_max_l):
        """Set detection threshold of the laser

        :param int length_min_l: int containing the min length that the laser will detect(mm), this value must be upper than 20 mm
        :param int length_max_l: int containing the max length that the laser will detect(mm), this value must be lower than 5600 mm
        """
        if not self.proxy:
            self.proxy = self.session.service("ALLaser")
        return self.proxy.setDetectingLength(length_min_l, length_max_l)

    def setOpeningAngle(self, angle_min_f, angle_max_f):
        """Set openning angle of the laser

        :param float angle_min_f: float containing the min value in rad, this value must be upper than -2.35619449
        :param float angle_max_f: float containing the max value in rad, this value must be lower than 2.092349795
        """
        if not self.proxy:
            self.proxy = self.session.service("ALLaser")
        return self.proxy.setOpeningAngle(angle_min_f, angle_max_f)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALLaser")
        return self.proxy.version()
