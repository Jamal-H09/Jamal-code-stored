#Jamal
# A simulation of the popular rock paper scissors game4 where the players playts agaisnt the computer

#Init
import random

#functions
def rps():
     player = 0 # variable for the scorebaord
     
     comp = 0
     tie = 0
     while True:
        print("WElCOME TO MY RPS GAME")
        pick = input("Pick Rock, Paper, Scissors :").lower() #allows the player to pick between the three choices
        if pick!= "Rock" or "Paper" or "Scissors": #invaild input if statement
            print("Input Invaild")
            break
        computer = random.randint(1,3) # picks a number and uses it to assign the RPS to the variable
        if computer == 1:
            computer = "Rock"
        elif computer == 2:
            computer = "Paper"
        elif computer == 3:
            computer = "Scissors"
        if pick == "Rock" and computer == "Paper": # creates the display of who wins and adds the score to keep count for loses, wins and ties
            print("Computer has won")
            comp = comp +1
        elif pick == "Rock" and computer == "Scissors":
            print("Player has won")
            player = player +1
        elif pick == "Rock" and computer == "Rock":
            print("game is a tie")
            tie = tie +1
        elif pick == "Paper" and computer == "Rock":
            print("Player has won")
            player = player +1

        elif pick == "Paper" and computer == "Scissors":
            print("Computer has won")
            comp = comp +1

        elif pick == "Paper" and computer == "Paper":
            print("game is a tie")
            tie = tie +1

        elif pick == "Scissors" and computer == "Rock":
            print("Computer has won")
            comp = comp +1

        elif pick == "Scissors" and computer == "Paper":
            print("Player has won")
            player = player +1

        elif pick == "Scissors" and computer == "Scissors":
            print("game is a tie")
            tie = tie +1
        print(f"Player score is {player}, Computer score is {comp}, Tie is {tie}") # display the scoreboard from player to computer to ties
        play = input("Would you like to play again? " ) # asks if they will like to keep playing if they chose not to then it breaks

        if play == "No":
            break





#Main
rps()
