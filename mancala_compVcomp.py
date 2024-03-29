import random
import datetime

# testing GitHub connection


#starting menu
print("")
print("Welcome to Mancala!")
print("")

startTime = datetime.datetime.now()
print(startTime)
print("")

# track system time??
# maybe create a bigger wile loop starting here...
startCommand = input("Enter 'y' to run a game. Enter 'q' to QUIT.")

if startCommand == "y":
    playing = True
    print("the game has begun...")
elif startCommand == "q":
    playing = False
    print("You have QUIT the game.")
else:
    playing = False
    print("Unexpected entry.  The game is over.")

startTime = datetime.datetime.now()
print(startTime)
print("")



#Next up...
#
# run through multiple games... keep track of winners

# *** the game needs to be reset ***

# make the random bin choice more sophisticated

winsByOne = 0
winsByTwo = 0


for gameNumber in range(100):
    moveCount = 1

    binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    playing = True

    playerOne = True

    messageCode = 0

    giveawayPile = -1

    lastRecipient = -1

    chosenBin = -1

    while(playing and moveCount < 101):

        # avoid printing
        """
        print("Move number " + str(moveCount))
        if playerOne: print("Player One's move...")
        else: print("Player Two's move...")

        message = ""
        if playerOne and messageCode == -2:
            message = "Invalid input. Try again, Player One."
        elif not(playerOne) and messageCode == -2:
            message = "Invalid input. Try again, Player Two."
        elif playerOne and messageCode == -1:
            message = "You must choose a non-empty bin, Player One."
        elif not(playerOne) and messageCode == -1:
            message = "You must choose a non-empty bin, Player Two."
        print("")
        print(message)
        print("")
        """
        messageCode = 0

        i = 0
        for element in binAmount:
            binAmount[i] = int(binAmount[i])
            if int(binAmount[i]) < 10:
                binAmount[i] = " " + str(binAmount[i])
            else:
                binAmount[i] = str(binAmount[i])
            i = i + 1
        # end of the for loop

        """
        if not(playerOne):
            print("        a    b    c    d    e    f")
        print("+----+----+----+----+----+----+----+----+")
        print("|    | "+ binAmount[12] +" | "+ binAmount[11] 
            +" | "+ binAmount[10] +" | "+ binAmount[9] 
            +" | "+ binAmount[8] +" | "+ binAmount[7] +" |    |")
        print("| "+ binAmount[13] +" |----+----+----+----+----+----| "+ binAmount[6] +" |")
        print("|    | "+ binAmount[0] +" | "+ binAmount[1] 
            +" | "+ binAmount[2] +" | "+ binAmount[3] 
            +" | "+ binAmount[4] +" | "+ binAmount[5] +" |    |")
        print("+----+----+----+----+----+----+----+----+")
        if playerOne:
            print("        f    e    d    c    b    a")
        print("")
        """

        #userInput = input("Enter a letter to choose a bin or enter 'q' to QUIT: ")

        # choosing a bin at random
        userInput = random.choice(["a","b","c","d","e","f"])

        if userInput == "q":
            playing = False
            chosenBin = 0
        elif playerOne and userInput == "a":
            chosenBin = 5
        elif playerOne and userInput == "b":
            chosenBin = 4
        elif playerOne and userInput == "c":
            chosenBin = 3
        elif playerOne and userInput == "d":
            chosenBin = 2
        elif playerOne and userInput == "e":
            chosenBin = 1
        elif playerOne and userInput == "f":
            chosenBin = 0
        elif not(playerOne) and userInput == "a":
            chosenBin = 12
        elif not(playerOne) and userInput == "b":
            chosenBin = 11
        elif not(playerOne) and userInput == "c":
            chosenBin = 10
        elif not(playerOne) and userInput == "d":
            chosenBin = 9
        elif not(playerOne) and userInput == "e":
            chosenBin = 8
        elif not(playerOne) and userInput == "f":
            chosenBin = 7
        else:
            chosenBin = -2
            messageCode = -2  # invalid input



        if int(chosenBin) >= 0:
            giveawayPile = binAmount[chosenBin]
            binAmount[chosenBin] = 0
            if int(giveawayPile) <= 0:
                messageCode = -1  # empty bin was chosen

        recipient = chosenBin + 1
        while(int(giveawayPile) > 0):
            if(playerOne and int(recipient) == 13):
                recipient = 0
            if(not(playerOne) and int(recipient) == 6):
                recipient = 7

            binAmount[recipient] = int(binAmount[recipient]) + 1
            giveawayPile = int(giveawayPile) - 1
            
            if int(giveawayPile) == 0:
                lastRecipient = recipient
            else:
                recipient = int(recipient) + 1
                if int(recipient) > 13:
                    recipient = 0

        if(playerOne and int(lastRecipient) == 6):
            playerOne = True
        elif(playerOne and int(binAmount[lastRecipient]) == 1 and int(lastRecipient) < 6):
            binAmount[6] = int(binAmount[6]) + int(binAmount[lastRecipient]) + int(binAmount[12 - int(lastRecipient)])
            binAmount[lastRecipient] = 0
            binAmount[12 - int(lastRecipient)] = 0
            playerOne = not(playerOne)
        elif(not(playerOne) and int(lastRecipient) == 13):
            playerOne = False
        elif(not(playerOne) and int(binAmount[lastRecipient]) == 1 and int(lastRecipient) > 6):
            binAmount[13] = int(binAmount[13]) + int(binAmount[lastRecipient]) + int(binAmount[12 - int(lastRecipient)])
            binAmount[lastRecipient] = 0
            binAmount[12 - int(lastRecipient)] = 0
            playerOne = not(playerOne)
        elif(int(messageCode) >= 0):
            playerOne = not(playerOne)

        # checking for the end of the game
        sideOne = 0
        sideTwo = 0
        for j in range(6):
            sideOne = int(sideOne) + int(binAmount[j])
            sideTwo = int(sideTwo) + int(binAmount[j+7])

        if(int(sideOne) == 0 or int(sideTwo) == 0):
            playing = False
            binAmount[6] = int(binAmount[6]) + int(sideOne)
            binAmount[13] = int(binAmount[13]) + int(sideTwo)
            for k in range(6):
                binAmount[k] = 0
                binAmount[k+7] = 0

        moveCount = int(moveCount) + 1



    # end of the while loop
    print("")
    print("Number of moves: " + str(moveCount))
    print("The game is over!")
    if int(binAmount[13]) < int(binAmount[6]):
        print("Player One has won the game!")
        winsByOne = winsByOne + 1
    elif int(binAmount[13]) > int(binAmount[6]):
        print("Player Two has won the game!")
        winsByTwo = winsByTwo + 1
    else:
        print("The game ended in a tie.")

    i = 0
    for element in binAmount:
        binAmount[i] = int(binAmount[i])
        if int(binAmount[i]) < 10:
            binAmount[i] = " " + str(binAmount[i])
        else:
            binAmount[i] = str(binAmount[i])
        i = i + 1
    # end of the for loop


    t = datetime.datetime.now()
    print("Time: " + str(t) + "  Game Number: " + str(gameNumber))
    print("")

print("")
print("Results...")
print("Start time: "+str(startTime))
print("End Time: "+str(t))
print("One: "+str(winsByOne))
print("Two: "+str(winsByTwo))

