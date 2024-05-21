''' rock, paper, scissors, by al sweigart
the classic hand game of luck against an opponent '''

import random
import time
import sys

print('''Rock, Paper, Scissors)
Rock beats scissors.
Scissors beats paper.
Paper beats rock.''')

# these variables track the wins, loss, and ties
WINS = 0
LOSSES = 0
TIES = 0

while True:     # main game loop
    while True:     # ask player until get input r, p, s, or q
        print(f'{WINS} Wins, {LOSSES} Losses, {TIES} Ties')
        print("Enter your move: (R)ock, (P)aper, (S)cissors, or (Q)uit")
        PLAYERMOVE = input("> ").upper()
        if PLAYERMOVE == "Q":
            print("Thanks for playing!")
            sys.exit()

        if PLAYERMOVE not in ("R" or "P" or "S"):
            print("Please type one of these choices: R, P, S, or Q.")

    # display the player's choice
        if PLAYERMOVE == "R":
            print("ROCK versus...")
            PLAYERMOVE = "ROCK"
        elif PLAYERMOVE == "P":
            print("PAPER vs...")
            PLAYERMOVE = "PAPER"
        elif PLAYERMOVE == "S":
            print("SCISSORS vs...")
            PLAYERMOVE = "SCISSORS"

        # countdown to 3 with dramatic pauses
        time.sleep(0.5)
        print("1...")
        time.sleep(0.25)
        print("2...")
        time.sleep(0.25)
        print("3...")
        time.sleep(0.25)

        # display the computer program's choice
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            COMPUTERMOVE = "ROCK"
        elif randomNumber == 2:
            COMPUTERMOVE = "PAPER"
        elif randomNumber == 3:
            COMPUTERMOVE = "SCISSORS"
        print(COMPUTERMOVE)
        time.sleep(0.50)

        # display and record the win, loss, or tie.
        if PLAYERMOVE == COMPUTERMOVE:
            print("It\'s a tie!")
            TIES += 1
        elif PLAYERMOVE == "ROCK" and COMPUTERMOVE == "SCISSORS":
            print("You win!")
            WINS +=1
        elif PLAYERMOVE == "PAPER" and COMPUTERMOVE == "ROCK":
            print("You win!")
            WINS +=1
        elif PLAYERMOVE == "SCISSORS" and COMPUTERMOVE == "PAPER":
            print("You win!")
            WINS +=1
        elif PLAYERMOVE == "ROCK" and COMPUTERMOVE == "PAPER":
            print("You lose!")
            LOSSES +=1
        elif PLAYERMOVE == "PAPER" and COMPUTERMOVE == "SCISSORS":
            print("You lose!")
            LOSSES +=1
        elif PLAYERMOVE == "SCISSORS" and COMPUTERMOVE == "ROCK":
            print("You lose!")
            LOSSES +=1
