import random
import datetime

#starting menu
print("")
print("Welcome to Mancala!")
print("")

# maybe create a bigger while loop starting here...
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

totalGames = 1
for gameNumber in range(totalGames):

    moveArray = [4,4,4,4,4,4,0,4,4,4,4,4,4,0,"player",0,"move","a","winner",0]
    gameArray = ["start"]
    gameArray.append(moveArray)
    k = 0
    for item in gameArray:
        #print(gameArray[k])
        print("i am here")
        k=k+1

    # need to figure out where to write into the gameRecord file???


    moveCount = 1

    binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    playing = True

    playerOne = True

    messageCode = 0

    giveawayPile = -1

    lastRecipient = -1

    chosenBin = -1

    while(playing and moveCount < 101):

        messageCode = 0

        # this for loop is probably unnecessary...
        i = 0
        for element in binAmount:
            binAmount[i] = int(binAmount[i])
            if int(binAmount[i]) < 10:
                binAmount[i] = " " + str(binAmount[i])
            else:
                binAmount[i] = str(binAmount[i])
            i = i + 1
        # end of the for loop


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

        # +----+----+----+----+----+----+----+----+
        # |    | 12 | 11 | 10 |  9 |  8 |  7 |    |
        # | 13 |----+----+----+----+----+----|  6 |
        # |    |  0 |  1 |  2 |  3 |  4 |  5 |    |
        # +----+----+----+----+----+----+----+----+
        

        if int(chosenBin) >= 0:
            # assign the chosen bin amount to the 'giveawayPile'
            giveawayPile = binAmount[chosenBin]

            # set up a signal if the giveawayPile is empty
            if int(giveawayPile) <= 0:
                messageCode = -1  # empty bin was chosen

            # record the move if a NON-Empty bin is chosen
            else:
                # add the current MOVE into the gameArray
                # then add a new moveArray to the gameArray
                gameArray[moveCount][17] = userInput
                if (playerOne):
                    gameArray[moveCount][15] = 1
                else:
                    gameArray[moveCount][15] = 2    
                j = 0
                for element in binAmount:
                    gameArray[moveCount][j]=int(binAmount[j])
                    j = j + 1
                print(gameArray[moveCount])
                moveCount = int(moveCount) + 1
                gameArray.append(moveArray)

            # empty the chosenBin
            binAmount[chosenBin] = 0
            

        # set the 'recipient' index to be the one next to the chosenBin
        recipient = chosenBin + 1
        
        # this WHILE loop gives away stones one by one until they are done
        while(int(giveawayPile) > 0):
            # adjust the recipient index if needed when a mancala is the recipient
            if(playerOne and int(recipient) == 13):
                recipient = 0
            if(not(playerOne) and int(recipient) == 6):
                recipient = 7

            # add one stone to the recipient and take one away from the giveawayPile
            binAmount[recipient] = int(binAmount[recipient]) + 1
            giveawayPile = int(giveawayPile) - 1
            
            if int(giveawayPile) == 0:
                lastRecipient = recipient
            else:
                recipient = int(recipient) + 1
                if int(recipient) > 13:
                    recipient = 0

        # stay with Player One if the last stone was placed in player One's mancala
        if(playerOne and int(lastRecipient) == 6):
            playerOne = True
        # if the last stone falls in an empty bin on Player One's side
        elif(playerOne and int(binAmount[lastRecipient]) == 1 and int(lastRecipient) < 6):
            binAmount[6] = int(binAmount[6]) + int(binAmount[lastRecipient]) + int(binAmount[12 - int(lastRecipient)])
            binAmount[lastRecipient] = 0
            binAmount[12 - int(lastRecipient)] = 0
            playerOne = not(playerOne)
        # stay with Player Two if the last stone was placed in Player Two's mancala
        elif(not(playerOne) and int(lastRecipient) == 13):
            playerOne = False
        # if the last stone falls in an empty bin on Player Two's side
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





    # end of the while loop
    
    #print("")
    #print("Number of moves: " + str(moveCount))
    #print("The game is over!")
    if int(binAmount[13]) < int(binAmount[6]):
        #print("Player One has won the game!")
        winsByOne = winsByOne + 1
    elif int(binAmount[13]) > int(binAmount[6]):
        #print("Player Two has won the game!")
        winsByTwo = winsByTwo + 1
    #else:
        #print("The game ended in a tie.")

        

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

# want to add file writing and reading to store info from the randomized games...

"""
with open("c:/workspace/mancala/testfile.txt", "w") as f:
    f.write("testing, testing\n")
    f.write("onto the next line...")
    f.write("and on and on.")

if f.closed:
    print("Case closed.")

"""