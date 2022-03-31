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
    cheatTime = 0.1;
    choiceTime = 0.55;

    def __init__(self, session):
        self.service = session.service("ALMotion")
        self.service.setIdlePostureEnabled("Body", False)
        self.service.setStiffnesses("Body", 0.5)
        self.service.setStiffnesses("Head", 1.0)
        self.service.setStiffnesses("RArm", 1.0)
        self.state = "rest"

    def makeChoice(self, choice):
        ''' 1 for even and 2 for odd '''
        if choice == 1:
            self.even(self.choiceTime)
        elif choice == 2:
            self.odd(self.choiceTime)
        time.sleep(0.2)

    def changeChoice(self):
        if self.state == 1:
            self.even(self.cheatTime)
        elif self.state == 0:
            self.odd(self.cheatTime)
        else:
            print("Unexpected case for toggle: " + self.state)
        time.sleep(0.2)

    def odd(self, time):
        self._setRArm(time, 1.04, -0.0, 0.88, 1.0, 1.8, 1.0)
        self.state = 1

    def even(self, time):
        self._setRArm(time, 1.04, -0.0, 0.88, 1.0, 1.8, 0.0)
        self.state = 0

    def rest(self):
        self._setRArm(0.7, 1.6, -0.1, 1.5, 0.2, 0.4, 0.5)
        self.state = "rest"

    def _setRArm(self, time, shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand):
        names = ["RShoulderPitch", "RShoulderRoll",
                "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
        angleLists = [[shoulderPitch],
                    [shoulderRoll],
                    [elbowYaw],
                    [elbowRoll],
                    [wristYaw],
                    [hand]]
        times = [time]
        timeLists = [times, times, times, times, times, times]
        isAbsolute = True
        self.service.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    def close(self):
        self.service.setIdlePostureEnabled("Body", True)

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
