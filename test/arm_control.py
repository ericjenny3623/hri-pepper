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
    motion_service.setStiffnesses("Body", 0.1)
    motion_service = session.service("ALMotion")


# Open palm
# ---------------------- Model - --------------------------
#         BodyName   Stiffness     Command      Sensor
#          HeadYaw    0.000000 - 0.131922 - 0.131922
#        HeadPitch    0.000000    0.445059    0.739379
#   LShoulderPitch    1.000000    1.581312    1.569262
#    LShoulderRoll    1.000000    0.143783    0.138058
#        LElbowYaw    1.000000   -1.218096   -1.211845
#       LElbowRoll    1.000000   -0.509870   -0.504680
#        LWristYaw    1.000000   -0.108126   -0.150374
#          HipRoll    1.000000   -0.022942   -0.027612
#         HipPitch    1.000000   -0.021623   -0.027612
#        KneePitch    1.000000    0.002908   -0.010738
#   RShoulderPitch    0.000000    1.306952    1.306952
#    RShoulderRoll    0.000000   -0.038350   -0.038350
#        RElbowYaw    0.000000    1.234855    1.234855
#       RElbowRoll    0.000000    1.210311    1.210311
#        RWristYaw    0.000000    1.624464    1.624464
#            LHand    1.000000    0.390608    0.414763
#            RHand    0.000000    0.479789    0.479789
#          WheelFL    0.000000    0.000000    0.000000
#          WheelFR    0.000000    0.000000    0.000000
#           WheelB    0.000000    0.000000    0.000000

# Palm down
# ---------------------- Model - --------------------------
#         BodyName   Stiffness     Command      Sensor
#          HeadYaw    0.000000 - 0.131922 - 0.131922
#        HeadPitch    0.000000    0.445059    0.739379
#   LShoulderPitch    1.000000    1.573484    1.576932
#    LShoulderRoll    1.000000    0.141162    0.141126
#        LElbowYaw    1.000000   -1.216226   -1.213379
#       LElbowRoll    1.000000   -0.507074   -0.516952
#        LWristYaw    1.000000   -0.100342   -0.138102
#          HipRoll    1.000000   -0.022942   -0.026078
#         HipPitch    1.000000   -0.021623   -0.027612
#        KneePitch    1.000000    0.002908   -0.010738
#   RShoulderPitch    0.000000    1.310020    1.310020
#    RShoulderRoll    0.000000   -0.024544   -0.024544
#        RElbowYaw    0.000000    1.231787    1.231787
#       RElbowRoll    0.000000    1.173496    1.173496
#        RWristYaw    0.000000   -1.566256   -1.566256
#            LHand    1.000000    0.371888    0.384886
#            RHand    0.000000    0.497364    0.497364
#          WheelFL    0.000000    0.000000    0.000000
#          WheelFR    0.000000    0.000000    0.000000
#           WheelB    0.000000    0.000000    0.000000




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
