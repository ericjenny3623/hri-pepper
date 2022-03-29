condition = "control"
#this is the random sequence generated by a python script
sequence = [2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2]

numRounds = 20
#control
if condition == "control":
    for i in range(numRounds):
        speech.say("Even or odd?")
        raw_input("Press Enter to continue") #wait for human to respond
        speech.say("3 2 1")

        if sequence[i] == "1":
            palmUp(motion_service)
        elif sequence[i] == "2":
            palmDown(motion_service)
        else:
            break
        option = raw_input("Press 1=win or 2=lose: ")
        if option == "1":
            speech.say("I win")
        elif option == "2":
            speech.say("I lose")
        else:
            break
#cheat occurs on 4th, 8th, and 15th rounds
#if can't cheat successfully, everything gets pushed back
else if condition == "cheat" or condition == "lose":
    cheatRounds = [4, 8, 15]
    for i in range(numRounds):
        speech.say("Even or odd?")
        raw_input("Press Enter to continue") #wait for human to respond
        speech.say("3 2 1")

        isUp = True
        if sequence[i] == "1":
            palmUp(motion_service)
        elif sequence[i] == "2":
            palmDown(motion_service)
            isUp = False
        else:
            break

        #cheating here!
        if i in cheatRounds:
            option = raw_input("Press 1=robot can cheat, press 2=robot cannot cheat")
            if option == "1":
                #switch the motion from up to down or down to up
                if isUp:
                    palmDown(motion_service)
                else:
                    palmUp(motion_service)
            else:
                #increment rounds so that everything gets pushed back
                numRounds = numRounds + 1
                for i in range(len(cheatRounds)):
                    if i <= cheatRounds[i]: #if the round has not passed
                        cheatRounds[i] = cheatRounds[i] + 1
            if condition == "cheat":
                speech.say("I win")
            else 
                speech.say("I lose")
else:
    print("Error: choose condition control, cheat, or lose")


