#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use angleInterpolation Method"""

import qi
import argparse
import sys
import time
import almath
from naoqi import ALProxy

pepper_ip = "128.237.247.249"

def main(session, speech):
    """
    This example uses the angleInterpolation method.
    """
    # Get the service ALMotion.
    motion_service = session.service("ALMotion")
    motion_service.setIdlePostureEnabled("Body", False)
    motion_service.setStiffnesses("Body", 1.0)
    motion_service.setStiffnesses("RArm", 1.0)
    palmUp(motion_service)
    time.sleep(2)
    rest(motion_service)
    time.sleep(2)
    palmDown(motion_service)
    time.sleep(2)
    rest(motion_service)
    motion_service.setIdlePostureEnabled("Body", True)


def palmUp(motion_service):
    setRArmv3(motion_service, 1.04, -0.0, 0.88, 1.0, 1.8, 1.0)


def palmDown(motion_service):
    setRArmv3(motion_service, 0.97, -0.0, 0.9, 1.0, -1.07, 1.0)

def fist(motion_service):
    setRArm(motion_service, 1.3, -0.03, 1.23, 1.17, 0, 0.0)

def rest(motion_service):
    setRArmv3(motion_service, 1.6, -0.1, 1.5, 0.2, 0.4, 0.5)

def setRArm(proxy, shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand):
    names = ["RShoulderPitch", "RShoulderRoll",
             "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[shoulderPitch, shoulderPitch, 1.615282],
              [shoulderRoll, shoulderRoll, -0.0874],
              [elbowYaw, elbowYaw, 1.463418],
              [elbowRoll, elbowRoll, 0.204020],
              [wristYaw, wristYaw, 0.420274],
              [hand, hand, 0.5]]
    times = [0.3, 4.0, 5.0]
    timeLists = [times, times, times, times, times, times]
    isAbsolute = True
    proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)


def setRArmNew(proxy, shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand):
    names = ["RShoulderPitch", "RShoulderRoll",
             "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand]
    proxy.setAngles(names, angleLists, 0.2)
    proxy.setAngles("RElbowRoll", elbowRoll, 0.7)


def setRArmv3(proxy, shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand):
    names = ["RShoulderPitch", "RShoulderRoll",
             "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[shoulderPitch],
                  [shoulderRoll],
                  [elbowYaw],
                  [elbowRoll],
                  [wristYaw],
                  [hand]]
    times = [0.4]
    timeLists = [times, times, [0.2], times, times, times]
    isAbsolute = True
    proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=pepper_ip,
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
              "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    tts = ALProxy("ALTextToSpeech", pepper_ip, 9559)

    main(session, tts)
