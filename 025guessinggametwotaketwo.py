#Practice Python 025 Guessing Game Two

#The user, inputs a number between 0 and 100. The program will guess a number, and you tell the program the guess is too high, too low, or your number.

import random
# too simple solution because python can repeat guesses.  It works.
# pythonguess = random.randint(1,10)
# print(pythonguess)
# usernumber = int(input("Enter a number for Python to guess: "))
# print(usernumber)
# pythoncounterguess = 1
# if pythonguess == usernumber:
# 	print("Python guessed your number.  Number of guesses:",pythoncounterguess)
# while pythonguess != usernumber:
# 	pythonguess = random.randint(1,10)
# 	print(pythonguess)
# 	if pythonguess == usernumber:
# 		print("Python guessed your number.  Number of guesses:",pythoncounterguess+1)
# 		break
# 	pythoncounterguess += 1

# pythonalreadyguessed = []
# pythonguess = random.randint(1,10)
# usernumber = int(input("Enter a number for Python to guess: "))
# print(usernumber)
# pythoncounterguess = 1
# if pythonguess == usernumber:
# 	print("Python guessed your number.  Number of guesses:",pythoncounterguess)
# pythonalreadyguessed.append(pythonguess)
# print(pythonalreadyguessed)
# while pythonguess != usernumber:	
# 	pythonguess = random.randint(1,10)
# 	pythonalreadyguessed.append(pythonguess)
# 	print(pythonguess)
# 	if pythonguess == usernumber:
# 		print("Python guessed your number.  Number of guesses:",pythoncounterguess+1)
# 		print(pythonalreadyguessed)
# 		break
# 	elif pythonguess >= usernumber:
# 		print("Python guess too high.  Guess lower")
# 	elif pythonguess <= usernumber:
# 		print("Python guess too low.  Guess higher")
# 	pythoncounterguess += 1

pythonnumberlist = []
for eachnumber in range(1,11):
	pythonnumberlist.append(eachnumber)
print(pythonnumberlist)
pythonnumberlistindexnumber = random.randint(0,len(pythonnumberlist))
pythonguess = pythonnumberlist[pythonnumberlistindexnumber]
print(pythonguess)
usernumber = int(input("Enter a number for Python to guess: "))
print(usernumber)
pythoncounterguess = 1
if pythonguess == usernumber:
	print("Python guessed your number.  Number of guesses:",pythoncounterguess)
pythonnumberlist.remove(pythonguess)
while pythonguess != usernumber:	
	pythonnumberlistindexnumber = random.randint(0,len(pythonnumberlist))
	pythonguess = pythonnumberlist[pythonnumberlistindexnumber]
	print(pythonguess)
	if pythonguess == usernumber:
		print("Python guessed your number.  Number of guesses:",pythoncounterguess+1)
		break
	elif pythonguess >= usernumber:
		print("Python guess too high.  Guess lower")
	elif pythonguess <= usernumber:
		print("Python guess too low.  Guess higher")
	pythonnumberlist.remove(pythonguess)
	pythoncounterguess += 1

# pythonnumberlist = []
# for eachnumber in range(1,11):
# 	pythonnumberlist.append(eachnumber)
# print(pythonnumberlist)
# removerandomnumber = random.randint(1,10)
# print(removerandomnumber)
# pythonnumberlist.remove(removerandomnumber)
# print(pythonnumberlist)



