#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use angleInterpolation Method"""

import qi
import time

pepper_ip = "128.237.247.249"


class Speech:
    cheatTime = 0.1
    choiceTime = 0.55

    def __init__(self, session):
        self.service = session.service("ALTextToSpeech")
        self.service.setParameter("speed", 100)

    def say(self, text):
        self.service.say(text)

    def lose(self):
        self.service.say("you win")

    def win(self):
        self.service.say("Yes, I win")

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

