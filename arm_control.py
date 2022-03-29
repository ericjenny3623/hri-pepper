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

    motion_service.setAngles("RElbowRoll", 0.4, 0.5)
    time.sleep(5)
    motion_service.setStiffnesses("Body", 1.0)

    # palmUp(motion_service)
    # palmDown(motion_service)

    posture_service = session.service("ALRobotPosture")
    posture_service.set
    # # Start breathing
    # motion_service.setBreathEnabled('Body', True)

    # motion_service.setIdlePostureEnabled("RArm", False)

    # # Let the robot breath
    # time.sleep(10)

    # # Stop breathing
    # motion_service.setBreathEnabled('Body', False)


def palmUp(motion_service):
    setRArm(motion_service, 1.3, -0.03, 1.23, 1.21, 1.62, 1.0)


def palmDown(motion_service):
    setRArm(motion_service, 1.3, -0.03, 1.23, 1.17, -1.56, 1.0)

def fist(motion_service):
    setRArm(motion_service, 1.3, -0.03, 1.23, 1.17, 0, 0.0)


def setRArm(proxy, shoulderPitch, shoulderRoll, elbowYaw, elbowRoll, wristYaw, hand):
    names = ["RShoulderPitch", "RShoulderRoll",
             "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [[shoulderPitch, shoulderPitch, 1.615282],
              [shoulderRoll, shoulderRoll, -0.0874],
              [elbowYaw, elbowYaw, 1.463418],
              [elbowRoll, elbowRoll, 0.204020],
              [wristYaw, wristYaw, 0.420274],
              [hand, hand, 0.5]]
    times = [0.5, 4.0, 5.0]
    timeLists = [times, times, times, times, times, times]
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
