from random import *
fourdigitnumber = randint(1000,10000)
# print("Cheat", fourdigitnumber)
# fourdigitnumberless = fourdigitnumber - 100
# print(fourdigitnumberless)
# fourdigitnumbergreater = fourdigitnumber + 100
# print(fourdigitnumbergreater)
cows = 0
bulls = 0
guess = 1
while guess != fourdigitnumber:
	guess = int(input("Enter a number between 1000 and 9999.  Enter 0 to quit: "))
	print(guess)
	if guess == 0:
		break
	elif guess == fourdigitnumber:
		print("Yes")
		cows += 1
		print("Bulls:",bulls, "Cows:",cows)
		break
	elif ((fourdigitnumber-100) < guess < (fourdigitnumber+100)):
		cows += 1
	else:
		bulls += + 1
	print("Bulls:",bulls, "Cows:",cows)