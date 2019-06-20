# Author: Sebastian Deluca
# Date: 4/18/2019
# File Name: Deluca_KetchupMustardMayo_RPS_3_4_4.py
# Description: Hamburger Condiment themed Rock Paper Scissors, where the user
#   is pitted against a computer in a game best of either, 1, 3, or 5, with
#   an active scoreboard visible.

import random # Access the random library
from easygui import * # Access easygui

def wS(times): # Whitespace function
    for amount in range(times): # A loop that repeats as much as i want it to
        print('') # Whitespace
        
def showMenu(): # Display the main menu
    mainMenuImage = 'Deluca_HomeScreen.png' # Set main menu image
    menuOptions = ['Play', 'Help', 'Quit'] # Set options
    userInput = buttonbox('W E L C O M E !' , 'Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = mainMenuImage, choices = menuOptions) # Welcome the user to the program
    return userInput # Return the user's choice to the program

def quitMenu(): # Display a quit menu
    quitOptions = ['Yes, I would like to quit.', 'No, return me to the main menu.'] # Set quit screen options
    userConfirm = buttonbox('Are you sure you want to quit?', 'Ketchup. Mustard. Mayonnaise! by Sebastian Deluca',choices = quitOptions) # Display quit screen to user
    if userConfirm == 'Yes, I would like to quit.': # if the user confirms they want to quit
        userQuit = True # Set this value to true
        return userQuit # Return this to the program

def nextStep(userInput): # Determine what to show the user
    if userInput == 'Help': # If the user wants help
        text = 'Hamburger-Condiment-Themed Rock, Paper Scissors! A revisiting of the classical elementary school game with a fun new twist. Instead of Rock, Paper and Scissors, you play with Ketchup, Mustard, and Mayonnaise. Ketchup beats Mayonnaise, Mustard Beats Ketchup, and Mayonnaise beats Mustard! To play, select the Play button on the main menu, and then select how many rounds you would like to play (You can choose from 1, 3, or 5.) Then, select your condiment by clicking the button with that condiments name on it in-game! All gamelengths will run the said-amount of rounds regardless of points. Whoever wins at the end wins. That is all you need to know, have fun!' # Set the message that will display in the text box
        msgbox(text,'Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', 'Scroll Down Before Continuing!' ) # Explain the program to the user

    elif userInput == 'Quit': # If the user wants to quit
        userInput = quitMenu() # Show the quit menu
        return userInput # Return this to the program
    else: # The user wants to play
        return userInput # Return this to the program

def getTurns(): # Get the amount of turns the user wants to do
    turnsImage = 'Deluca_TurnsScreen.png' # Set the turns screen image
    turnChoices = ['1 Turn', '3 Turns', '5 Turns'] # List of choices for turns
    turns = buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = turnsImage, choices = turnChoices) # Display a buttonbox with options for how long the game will run
    if turns == '1 Turn': # If the user wants one run
        turns = 1 # Make the turns equal 1
    elif turns == '3 Turns': # If the user wants best of 3
        turns = 2 # Make the amount of turns 3
    elif turns == '5 Turns': # If the user wants best of 5
        turns = 3 # Make the amount of turns 5
    return turns # Return this value to the program

def detImg(cpuChoice, userChoice): # Determines which image to display to the user
    ###KETCHUP V KETCHUP
    if userChoice == 1 and cpuChoice == 1: # If both choose ketchup
        vsImg = 'Deluca_KetchupVKetchup.png' # Set the image
    ###KETCHUP V MUSTARD
    elif userChoice == 1 and cpuChoice == 2: # If CPU chooses mustard
        vsImg = 'Deluca_KetchupVMustard.png' # Set the image
    ###KETCHUP V MAYO
    elif userChoice == 1 and cpuChoice == 3: # If the CPU chooses mayo
        vsImg = 'Deluca_KetchupVMayo.png' # Set the image
    ###MUSTARD V KETCHUP
    elif userChoice == 2 and cpuChoice == 1: # If cpu chose ketchup
        vsImg = 'Deluca_MustardVKetchup.png' # Set the image
    ###MUSTARD V MUSTARD
    elif userChoice == 2 and cpuChoice == 2: # If both choose mustard
        vsImg = 'Deluca_MustardVMustard.png' # Set the image
    ###MUSTARD V MAYO
    elif userChoice == 2 and cpuChoice ==3: # If cpu chose mayo
        vsImg = 'Deluca_MustardVMayo.png' # Set the image
    ###MAYO V KETCHUP
    elif userChoice == 3 and cpuChoice == 1: # If CPU chose ketchup
        vsImg = 'Deluca_MayoVKetchup.png' # Set the image
    ###MAYO V MUSTARD
    elif userChoice == 3 and cpuChoice == 2: # If CPU chose mayo
        vsImg = 'Deluca_MayoVMustard.png' # Set the image
    ###MAYO V MAYO
    elif userChoice == 3 and cpuChoice == 3: # If both chose mayo
        vsImg = 'Deluca_MayoVMayo.png' # Set the image
    return vsImg # Return the image to the program

def detWinner(userWin,cpuWin,turns): # A function that determines the winner of the game
    if turns == 2: # If the user wanted to do 3 rounds
        if userWin == cpuWin: # If the players tie
            drawImg = 'Deluca_DrawGame.png' # Set the image
            drawBtns = ['Return to Main Menu'] # Set the buttons
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = drawImg, choices = drawBtns) # Give the user the choice to play again or quit

        elif userWin == 3: # If the user wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif userWin == 2 and cpuWin <= 1: # If the user wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit
        elif userWin == 1 and cpuWin == 0: # If the user wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin == 3: # If the CPU wins
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin == 2 and userWin >= 1: #If the cpu won
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin == 1 and userWin == 0: # If the cpu won
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit
        elif userWin > cpuWin: # If the user has the most wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin > userWin: # If the cpu has the most wins
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit
        
    elif turns == 3: # If the user wants to do 3 rounds
        if userWin == 5: # If the user wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif userWin == 4 and cpuWin <= 3: # If the user wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin == 5: # If the CPU wins
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit

        elif userWin == 4 and cpuWin <=3: # If the user wins
            drawImg = 'Deluca_DrawGame.png' # Set the image
            drawBtns = ['Return to Main Menu'] # Set the buttons
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = drawImg, choices = drawBtns) # Give the user the choice to play again or quit

        elif userWin == 4 and cpuWin == 4: # If the players tie
            drawImg = 'Deluca_DrawGame.png' # Set the image
            drawBtns = ['Return to Main Menu'] # Set the buttons
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = drawImg, choices = drawBtns) # Give the user the choice to play again or quit

        elif userWin > cpuWin: # If the user has the most wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin > userWin: # If the cpu has the most wins
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin == userWin: # If the players are tied
            drawImg = 'Deluca_DrawGame.png' # Set the image
            drawBtns = ['Return to Main Menu'] # Set the buttons
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = drawImg, choices = drawBtns) # Give the user the choice to play again or quit

    else: # If theres one turn
        if userWin == 1: # If the user wins
            userWinsImage = 'Deluca_userWinsGame.png' # Set Image
            userWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = userWinsImage, choices = userWinsButtons) # Give the user the choice to play again or quit

        elif cpuWin == 1: # If the CPU wins
            cpuWinsImage = 'Deluca_CPUWinsGame.png' # Set Image
            cpuWinsButtons = ['Return to Main Menu'] # Set options for buttonbox
            buttonbox('','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = cpuWinsImage, choices = cpuWinsButtons) # Give the user the choice to play again or quit

    msgbox('The final score was ' + str(cpuWin) + ' points for the computer, and ' + str(userWin) + ' points for You.') # Tell the user the final score
    playAgain = True # Make a boolean
    return playAgain # Return this boolean to the program

def runGame(turns, versusImg): # A function that runs the game
    userWin = 0 # Base total for rounds the user wins
    cpuWin = 0 # Base total for rounds the CPU wins
    drawCount = 0 # Base total for draws
    for runs in range(turns): # A loop that repeats either once, three times, or five times
        print('----------')
        print('r')
        print(runs)
        print('cpu')
        print(cpuWin)
        print('usr')
        print(userWin)
        print('TURNS')
        print(turns)
        flag = True # Activate flag
        while flag == True: # When the flag is running
            if drawCount == 2: # If theres 2 draws
                drawCount = 0 # Reset the counter
                turns += 1 # Extend the game
            else:
                cpuMove = getCPUMove() # Generate a choice for the computer's move
                userMove = getUserMove(cpuWin, userWin) # Get the user's move
                if cpuMove == 1: # If the CPU chooses ketchup
                    cpuChoice = 'Ketchup' # Set the string
                elif cpuMove == 2: # If the CPU chooses mustard
                    cpuChoice = 'Mustard' # Set the string
                elif cpuMove == 3: # If the CPU chooses mayo
                    cpuChoice = 'Mayonnaise' # Set the string
                if userMove == 1: # If the user chooses ketchup
                    userChoice = 'Ketchup' # Set the string
                elif userMove == 2: # If the user chooses mustard
                    userChoice = 'Mustard' # Set the string
                elif userMove == 3: # If the user chooses mayo
                    userChoice = 'Mayonnaise' # Set the string
                playImg = detImg(cpuMove, userMove) # Choose which picture to display
                btns = ['Go!'] # Set the buttons
                vsTxt = ('YOU(Left): ' + str(userChoice) + ' VERSUS COMPUTER(Right): ' + str(cpuChoice))
                buttonbox(vsTxt,'Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = playImg, choices = btns) # Create a button box to show what each player chose
                results = compareResults(cpuMove, userMove) # Determine who the winner is
                if cpuWin == 3 or userWin == 3: # If someone has won the 5 point game
                    runs = 4 # Stop the game
                    winner = detWinner(userWin, cpuWin, turns)# Call the detWinner function
                    return winner # Return this to the program
                else: # If nobody has won the 5 turn game
                    if results == 'CPU': # If the CPU won
                        flag = False # Stop the flag
                        cpuWin += 1 # Add 1 to the cpu win counter
                        buttons = ['OK!'] # Set buttons for the buttonbox
                        cpuImage = 'Deluca_CPUWin.png' # Set the image for the button box
                        buttonbox('The computer wins the round and gets one point!','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', choices = buttons, image = cpuImage) # Display a pop-up box telling the user the CPU wins
                    elif results == 'USER': # If the user won
                        flag = False # Stop the flag
                        userWin += 1 # Add 1 to the user win counter
                        buttons = ['OK!'] # Set buttons for the buttonbox
                        userImage = 'Deluca_USERWin.png' # Set the image for the button box
                        buttonbox('You win the round and get one point!','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', choices = buttons, image = userImage) # Display a pop-up box telling the user the CPU wins
                    else: # If it was a draw
                        drawCount+= 1 # Add to draw counter
                        buttons = ['OK!'] # Set the buttons
                        drawImage = 'Deluca_drawTurn.png' # Set the image
                        buttonbox('That round was a tie. Go again!','Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = drawImage, choices = buttons) # Tell the user that they tied
                if turns == 2 and runs == 1 and (cpuWin >= 2 or userWin >= 2): # If there's 3 turns
                    runs = 2 # Stop the game
                    winner = detWinner(userWin, cpuWin, turns)# Call the detWinner function
                    return winner # Return this to the program
                
                elif turns == 3 and runs == 2 and (cpuWin >= 3 or userWin >=3): # If theres 5 turns
                    runs = 4 # Stop the game
                    winner = detWinner(userWin, cpuWin, turns)# Call the detWinner function
                    return winner # Return this to the program
        
def getCPUMove(): # A function that generates a random move for the computer
    cpuMove = random.randint(1,3) # Generate a random number between 1 and 3
    return cpuMove # Return the value of the cpu's random move

def getUserMove(cpu, user): # A function that gets the user input for what move they will do
    moveImage = 'Deluca_moveScreen.png' # Set the image
    choices = ['Ketchup', 'Mustard', 'Mayonnaise', 'Random'] # Choices for either rock paper or scissors
    userMove = buttonbox(('The Computer has ' + str(cpu) + ' points, You have ' + str(user) + ' points.'), 'Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', image = moveImage, choices = choices) # A button box to get the user moves
    if userMove == 'Ketchup': # If the user chose rock
        userMove = 1 # Set the value to one

    elif userMove == 'Mustard': # If the user chose Paper
        userMove = 2 # Set the value to two

    elif userMove == 'Mayonnaise': # If the user chose scissors
        userMove = 3 # Set the value to three

    else: # If the user chose random
        userMove = random.randint(1,3) # Generate a random number between 1 and 3
    return userMove # Return the value to the program

def compareResults(cpuMove, userMove): # A function that determines the winner of each round
    ###BOT WIN IFS
    if cpuMove == 1 and userMove == 3: # If the cpu does rock, and user does scissors
        winner = 'CPU' # Tell the runGame function that the CPU has won

    elif cpuMove == 2 and userMove == 1: # If the CPU does paper, and the user does Rock
        winner = 'CPU' # Tell the runGame function that the cpu has won

    elif cpuMove == 3 and userMove == 2: # If the CPU does scissors and the user does Paper
        winner = 'CPU' # Tell the runGame function that the CPU has won
    ###USER WIN IFS
    elif userMove == 1 and cpuMove == 3: # If the cpu does rock, and user does scissors
        winner = 'USER' # Tell the runGame function that the CPU has won

    elif userMove == 2 and cpuMove == 1: # If the CPU does paper, and the user does Rock
        winner = 'USER' # Tell the runGame function that the cpu has won

    elif userMove == 3 and cpuMove == 2: # If the CPU does scissors and the user does Paper
        winner = 'USER' # Tell the runGame function that the CPU has won

    else: # If the CPU and the user do the same thing
        winner = 'DRAW' # Tell the runGame function that nobody won
    return winner # Return the string to the runGame function

#############
vs = 'vs' # Set the versus image
#############

####PROGRAM RUNNING####
menuFlag = True # Activate main menu flag
while menuFlag == True: # When the main menu is showing
    userInput = showMenu() # Show the user the main menu
    userDoes = nextStep(userInput) # Determine whether to show the user help, quit, or begin the game
    if userDoes == 'Play': # If the user is ready to play
        menuFlag = False # Stop main menu flag
        turns = getTurns() # Get the number of turns the user wants to play
        menuFlag = runGame(turns, vs) # Run the game
    elif userDoes == True: # if the user wants to quit
        msgbox('Thank you for playing!', 'Ketchup. Mustard. Mayonnaise! by Sebastian Deluca', 'Goodbye!') # Close the game
        menuFlag = False # Stop the menu flag
