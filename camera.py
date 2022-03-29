#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use angleInterpolation Method"""

import qi
import argparse
import sys
import time
import almath
import cv2

pepper_ip = "128.237.247.249"

def main(session):
    """
    This example uses the angleInterpolation method.
    """
    # Get the service ALMotion.

    camera_service = session.service("ALVideoDevice")
    name = "test"
    cameraIndex = 1
    resolution = 1  # 0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA
    colorSpace = 11  # 0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR
    fps = 10
    camera_service.subscribeCamera(name, cameraIndex, resolution, colorSpace, fps)
    print(camera_service.getSubscribers())
    for i in range(0,1000):
        img = camera_service.getImageRemote(name)
        print(img)
        cv2.imshow("frame", img)
        time.sleep(1/fps)


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
