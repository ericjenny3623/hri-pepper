import ArmControl
import GazeAndPostureControl
import qi
import argparse
import sys
import time
import almath
from naoqi import ALProxy

pepper_ip = "128.237.247.249"

def main(condition, session, speech):
    """
    This example uses the angleInterpolation method.
    """
    # Get the service ALMotion.
    arm = ArmControl.ArmControl(session)
    gp = GazeAndPostureControl.GazeAndPostureControl(session)
    speech.setParameter("speed", 100)
    cheatRounds = [1, 8, 15]  # cheat occurs on 4th, 8th, and 15th rounds

    #this is the random sequence generated by a python script
    sequence = [2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2]

    numRounds = 20
    #control
    try:
        user = raw_input("Wait to start main game (enter to continue, q exits)")
        speech.say("Hi. Let's play a game of even and odd.")
        if user == "q":
                raise StopException()
        for i in range(numRounds):
            speech.say("Even or odd?")
            user = raw_input("Wait for response (enter to continue, q exits)") #wait for human to respond
            if user == "q":
                raise StopException()
            speech.say("3 2 1")

            arm.makeChoice(sequence[i])

            if condition == "control" or i not in cheatRounds:
                # We are not cheating
                sayWinner(speech)
            else:
                option = raw_input("Press 1=robot can cheat, press 2=robot cannot cheat")
                if option == "1":
                    arm.changeChoice()
                else:
                    #increment rounds so that everything gets pushed back
                    numRounds = numRounds + 1
                    cheatRounds = [rnd+1 if rnd >= i else rnd for rnd in cheatRounds]
                    # for i in range(len(cheatRounds)):
                    #     if i <= cheatRounds[i]: #if the round has not passed
                    #         cheatRounds[i] = cheatRounds[i] + 1
                if condition == "cheat":
                    speech.say("Yes, I win")
                else:
                    speech.say("Aw, you win")
            arm.rest()
        speech.say("Thank you for playing with me. Please fill out the survey on the laptop.")
    except StopException:
        print("Quitting")
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, going to try to close everything normally")
        print("Interrupt again if this hangs")
    arm.close()
    gp.close()

def sayWinner(tts):
    option = raw_input("Press 1=win or 2=lose: ")
    if option == "1":
        tts.say("Yes, I win")
    elif option == "2":
        tts.say("Aw, you win")
    elif option == "q":
        raise StopException()

def practice(condition, session, speech):
    user = raw_input("Wait to start practice rounds (enter to continue, q exits)")
    if user == "q":
        raise StopException()
    sequence = [1, 2]
    numRounds = 2
    for i in range(numRounds):
        speech.say("Even or odd?")
        user = raw_input("Wait for response (enter to continue, q exits)") #wait for human to respond
        if user == "q":
            raise StopException()
        speech.say("3 2 1")
        arm.makeChoice(sequence[i])
        # We are not cheating
        sayWinner(speech)


def trust():
    user = raw_input("Wait to start trust round (enter to continue, q exits)")
    speech.say("Let's play a final round of even and odd. I am going to throw a zero.")
    if user == "q":
        raise StopException()
    numRounds = 1
    speech.say("Even or odd?")
    user = raw_input("Wait for response (enter to continue, q exits)") #wait for human to respond
    if user == "q":
        raise StopException()
    speech.say("3 2 1")
    arm.makeChoice(1)
    sayWinner(speech)
    
class StopException(Exception):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=pepper_ip,
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--cond", type=str, default="control",
                        help="Condtion: control, cheat, or lose")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
              "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    tts = ALProxy("ALTextToSpeech", pepper_ip, 9559)

    print("This is the practice session")
    print("This is the main game")
    main(args.cond, session, tts)
    print("This is the trust test")
