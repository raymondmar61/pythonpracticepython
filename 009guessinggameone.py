import random
numbertoguess = random.randint(1,9)
print("Cheat" ,numbertoguess)

while True:
	numberguess = int(input("Guess the number from 1 to 9.  Enter 0 to quit. "))
	if numberguess == 0:
		break
	if numberguess == numbertoguess:
		print("You guessed correctly", numbertoguess,"Let's play again.")
		numbertoguess = random.randint(1,9)
		print("Cheat" ,numbertoguess)
	elif numberguess > numbertoguess:
		print("Too high.  Guess again.")
	elif numberguess < numbertoguess:
		print("Too low.  Guess again.")

#sample solution
# import random
# number = random.randint(1,9)
# guess = 0
# count = 0
# while guess != number and guess != "exit":
# 	guess = input("What's your guess?")
# 	if guess == "exit":
# 		break
# 	guess = int(guess)
# 	count += 1
# 	if guess < number:
# 		print("Too low!")
# 	elif guess > number:
# 		print("Too high!")
# 	else:
# 		print("You got it!")
# 		print("And it only took you",count,"tries!")

#Extras:
# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.