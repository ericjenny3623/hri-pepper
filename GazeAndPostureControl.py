#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use angleInterpolation Method"""

import qi
import argparse
import sys
import time
from naoqi import ALProxy

pepper_ip = "128.237.247.249"


class GazeAndPostureControl:

    def __init__(self, session):
        self.tracker = session.service("ALTracker")
        self.posture = session.service("ALRobotPosture")
        self.posture.applyPosture("Stand", 1.0)

        targetName = "Face"
        faceWidth = 0.2
        self.tracker.registerTarget(targetName, faceWidth)
        self.tracker.track(targetName)

    def close(self):
        self.tracker.stopTracker()
        self.tracker.unregisterAllTargets()


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

    ctrl = GazeAndPostureControl(session)
    time.sleep(20.0)
    ctrl.close()