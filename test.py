#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use angleInterpolation Method"""

import qi
import argparse
import sys
import time
import almath

pepper_ip = "128.237.247.249"

def main(session):
    """
    This example uses the angleInterpolation method.
    """
    # Get the service ALMotion.

    motion_service = session.service("ALMotion")
    # tracker_service = session.service("ALTracker")
    # posture_service = session.service("ALRobotPosture")

    # posture_service.applyPosture("Stand", 1.0)

    # targetName = "Face"
    # faceWidth = 0.2
    # tracker_service.registerTarget(targetName, faceWidth)

    # # Then, start tracker.
    # tracker_service.track(targetName)

    # print("ALTracker successfully started, now show your face to robot!")
    # time.sleep(15)
    # # Stop tracker.
    # tracker_service.stopTracker()
    # tracker_service.unregisterAllTargets()
    motion_service.setStiffnesses("Body", 0.5)
    motion_service.setStiffnesses("RArm", 0.5)
    motion_service.setStiffnesses("Head", 0.5)
    motion_service.setIdlePostureEnabled("Body", False)

    time.sleep(1.0)
    print(motion_service.getSummary())

    # posture_service.applyPosture("Stand", 1.0)
    # motion_service.setBreathEnabled('Body', True)


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
    main(session)
