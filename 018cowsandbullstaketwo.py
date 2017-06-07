#Practice Python 018 Cows And Bulls
#Create a program that will play the “cows and bulls” game with the user. The game works like this: Randomly generate a 4digit number. Ask the user to guess a 4digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.  Add exercise description 051717.

import random
# computernumber = random.randint(1000,9999)
# print(computernumber)
# computernumberstring = str(computernumber)
# print(computernumberstring)
# computernumberlist = []
# for eachnumber in computernumberstring:
# 	computernumberlist.append(eachnumber)
# print(computernumberlist)

# usernumber = input("Enter a number: ")
# print(usernumber)
# usernumberlist = []
# for eachnumber in usernumber:
# 	usernumberlist.append(eachnumber)
# print(usernumberlist)

# userguess = 0
# while computernumberlist != usernumberlist:
# 	cows = 0
# 	bulls = 0
# 	for eachindex in range(0,len(computernumberlist)):
# 		if (computernumberlist[eachindex] == usernumberlist[eachindex]):
# 			cows = cows + 1
# 		elif (computernumberlist[eachindex] != usernumberlist[eachindex]):
# 			bulls = bulls + 1
# 	print("Cows:",cows, "Bulls:",bulls)
# 	usernumber = input("Guess again.  Enter a number: ")
# 	usernumberlist = []
# 	for eachnumber in usernumber:
# 		usernumberlist.append(eachnumber)
# 	userguess +=1
# print(usernumberlist)
# print("Correct",computernumber,"Guesses: ",userguess)

computernumber = random.randint(1000,9999)
computernumberstring = str(computernumber)
computernumberlist = []
for eachnumber in computernumberstring:
	computernumberlist.append(eachnumber)
print("Cheat",computernumberlist)

usernumber = input("Enter a number: ")
usernumberlist = []
for eachnumber in usernumber:
	usernumberlist.append(eachnumber)

userguess = 0
while computernumberlist != usernumberlist:
	cows = 0
	bulls = 0
	for eachindex in range(0,len(computernumberlist)):
		if (computernumberlist[eachindex] == usernumberlist[eachindex]):
			cows = cows + 1
		else (computernumberlist[eachindex] != usernumberlist[eachindex]):
			bulls = bulls + 1
	print("Cows:",cows, "Bulls:",bulls)
	usernumber = input("Guess again.  Enter a number: ")
	usernumberlist = []
	for eachnumber in usernumber:
		usernumberlist.append(eachnumber)
	userguess +=1
print("Correct",computernumber,"Guesses: ",userguess)
