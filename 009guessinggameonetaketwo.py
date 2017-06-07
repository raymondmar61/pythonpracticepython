#Practice Python 009 Guessing Game One
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.  Add exercise description 051717.

# import random
# playernumber = input("Guess a number between 1 and 9.  Type \"exit\" to quit.")
# computernumber = random.randint(1,9)
# guesscount = 1
# while playernumber != "exit":
# 	print(computernumber)
# 	if int(playernumber) == computernumber:
# 		print("You guessed correctly.")
# 		break
# 	elif int(playernumber) >= computernumber:
# 		print("Too high.")
# 		guesscount += 1
# 	elif int(playernumber) <= computernumber:
# 		print("Too low.")
# 		guesscount += 1
# 	else:
# 		print("Invalid guess input.")
# 	playernumber = input("Guess a number between 1 and 9.  Type \"exit\" to quit.")
# print("Guess count",guesscount)

import random
playernumber = input("Guess a number between 1 and 9.  Type \"exit\" to quit.")
computernumber = random.randint(1,9)
guesscount = 1
while playernumber != "exit":
	try:
		print(computernumber)
		if int(playernumber) == computernumber:
			print("You guessed correctly.")
			break
		elif int(playernumber) >= computernumber:
			print("Too high.")
			guesscount += 1
		elif int(playernumber) <= computernumber:
			print("Too low.")
			guesscount += 1
		else:
			print("Invalid guess input.")
		playernumber = input("Guess a number between 1 and 9.  Type \"exit\" to quit.")
	except ValueError:
		print("Make sure and enter a number.  Restart the program.")
		break
print("Guess count",guesscount)