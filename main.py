import ArmControl
import GazeAndPostureControl
import Speech
import qi
import argparse
import sys

pepper_ip = "128.237.247.249"

def main(condition, arm, speech):
    """
    This example uses the angleInterpolation method.
    """

    cheatRounds = [2, 5, 8]  # cheat occurs on 4th, 8th, and 15th rounds

    #this is the random sequence generated by a python script
    sequence = [2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2]

    waitToStart(" main game")

    speech.say("Hi. Let's play a game of even and odd.")

    for i in range(numRounds):
        speech.say("Even or odd?")
        waitToStart(" for response")
        speech.say("3 2 1")

        arm.makeChoice(sequence[i])

        if condition == "control" or i not in cheatRounds:
            # We are not cheating
            sayWinner(speech)
        else:
            option = raw_input("Press 1=win or 2=lose: ")
            if condition == "cheat" and option == "2":
                arm.changeChoice()
                speech.win()
            elif condition == "lose" and option == "1":
                arm.changeChoice()
                speech.lose()
            else:
                if option == "1":
                    speech.win()
                elif option == "2":
                    speech.lose()
                #increment rounds so that everything gets pushed back
                numRounds = numRounds + 1
                cheatRounds = [rnd+1 if rnd >= i else rnd for rnd in cheatRounds]
        arm.rest()
    speech.say("Thank you for playing with me. Please fill out the survey on the laptop.")

def waitToStart(text):
    user = raw_input("Wait (enter to continue, q exits) " + text)
    if user == "q":
        raise StopException()

def sayWinner(speech):
    option = raw_input("Press 1=win or 2=lose: ")
    if option == "1":
        speech.win()
    elif option == "2":
        speech.lose()
    elif option == "q":
        raise StopException()


def practice(arm, speech):
    waitToStart(" practice rounds")
    sequence = [1, 2]
    numRounds = 2
    for i in range(numRounds):
        speech.say("Even or odd?")
        waitToStart(" for response")
        speech.say("3 2 1")
        arm.makeChoice(sequence[i])
        # We are not cheating
        sayWinner(speech)
        arm.rest()


def trust(arm, gaze, speech):
    waitToStart(" trust condition")
    speech.say("Let's play a final round of even and odd. I am going to throw a zero.")
    numRounds = 1
    speech.say("Even or odd?")
    waitToStart(" for response")
    speech.say("3 2 1")
    arm.makeChoice(1)
    sayWinner(speech)
    arm.rest()

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

    arm = ArmControl.ArmControl(session)
    gp = GazeAndPostureControl.GazeAndPostureControl(session)
    speech = Speech.Speech(session)

    try:
        print("========== Practice Session ==========")
        practice(arm, speech)
        print("========== Main Game ==========")
        main(args.cond, arm, speech)
        print("========== Trust Test ==========")
        trust(arm, speech)

    except StopException:
        print("Quitting")
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, going to try to close everything normally")
        print("Interrupt again if this hangs")
    arm.close()
    gp.close()


