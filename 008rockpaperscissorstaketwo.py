#Practice Python 008 Rock Paper Scissors

import random
playerchoice = input("rock, paper, or scissors?  Type quit to exit. ")
while playerchoice != "quit":
	computerchoice = ["rock","paper","scissors"]
	indexnumber = random.randint(0,2)
	computerchoice = computerchoice[indexnumber]
	print(computerchoice)
	if playerchoice == "rock" and computerchoice == "rock":
		print("You choose rock and computer choose rock.  Tie")
	elif playerchoice == "rock" and computerchoice == "paper":
		print("You choose rock and computer choose paper.  You lose.")
	elif playerchoice == "rock" and computerchoice == "scissors":
		print("You choose rock and computer choose scissors.  You win.")
	elif playerchoice == "paper" and computerchoice == "rock":
		print("You choose paper and computer choose rock.  You win.")
	elif playerchoice == "paper" and computerchoice == "paper":
		print("You choose paper and computer choose paper.  You tie.")
	elif playerchoice == "paper" and computerchoice == "scissors":
		print("You choose paper and computer choose scissors.  You lose.")
	elif playerchoice == "scissors" and computerchoice == "rock":
		print("You choose scissors and computer choose rock.  You lose.")
	elif playerchoice == "scissors" and computerchoice == "paper":
		print("You choose scissors and computer choose paper.  You win.")
	elif playerchoice == "scissors" and computerchoice == "scissors":
		print("You choose scissors and computer choose scissors.  You tie.")
	else:
		print("Invalid input.  Try again below.")
	playerchoice = input("rock, paper, or scissors?  Type quit to exit. ")