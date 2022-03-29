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

    motion_service.setStiffnesses("Body", 1.0)
    # Example showing a single trajectory for one joint
    # Interpolates the head yaw to 1.0 radian and back to zero in 2.0 seconds
    # names = "LElbowRoll"
    # angleLists = [-70.0*almath.TO_RAD, -70.0*almath.TO_RAD, 0.0]
    # #              2 times
    # timeLists = [1.0, 4.0, 5]
    # isAbsolute = True
    # motion_service.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    setRArm(motion_service, 1.3, -0.03, 1.23, 1.21, 1.62, 1.0)
    setRArm(motion_service, 1.3, -0.03, 1.23, 1.17, -1.56, 1.0)
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
    times = [1.0, 4.0, 5.0]
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
