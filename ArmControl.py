#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use angleInterpolation Method"""

import qi
import argparse
import sys
import time
from naoqi import ALProxy

pepper_ip = "128.237.247.249"

class ArmControl:

    def __init__(self, session):
        self.service = session.service("ALMotion")
        self.service.setIdlePostureEnabled("Body", False)
        self.service.setStiffnesses("Body", 1.0)
        self.service.setStiffnesses("RArm", 1.0)
        self.state = "rest"

    def changeChoice(self):
        if self.state == "up":
            self.palmDown()
        elif self.state == "down":
            self.palmUp()
        else:
            print("Unexpected case for toggle: " + self.state)
        time.sleep(0.4)

    def palmUp(self):
        self._setRArm(1.04, -0.0, 0.88, 1.0, 1.8, 1.0)
        self.state = "up"

    def palmDown(self):
        self._setRArm(0.97, -0.0, 0.9, 1.0, -1.07, 1.0)
        self.state = "down"

    def fist(self):
        self._setRArm(1.3, -0.03, 1.23, 1.17, 0, 0.0)
        self.state = "fist"

    def rest(self):
        self._setRArm(1.6, -0.1, 1.5, 0.2, 0.4, 0.5)
        self.state = "rest"

    def _setRArm(self, shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand):
        names = ["RShoulderPitch", "RShoulderRoll",
                "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
        angleLists = [[shoulderPitch],
                    [shoulderRoll],
                    [elbowYaw],
                    [elbowRoll],
                    [wristYaw],
                    [hand]]
        times = [0.42]
        timeLists = [times, times, times, times, times, times]
        isAbsolute = True
        self.service.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(0.5)

    def close(self):
        pass

if __name__ == "__main__":
    pepper_ip = "128.237.247.249"
    port = "9559"
    session = qi.Session()
    try:
        session.connect("tcp://" + pepper_ip + ":" + "9559")
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"" + pepper_ip + "\" on port " + port + ".\n"
              "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    ctrl = ArmControl(session)
    ctrl.palmUp()
    time.sleep(2)
    ctrl.rest()
    time.sleep(2)
    ctrl.palmDown()
    time.sleep(2)
    ctrl.rest()
