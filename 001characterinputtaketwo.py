#Practice Python 001 Character Input
#input strings types int
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.  Add exercise description 051717.

from datetime import datetime
now = datetime.now()
current_year = now.year

# name = ""
# while name != "stop":
# 	name = input("Enter your name.  Type \"stop\" to end: ")
# 	if (name == "stop"):
# 		break
# 	age = int(input("Enter your age: "))
# 	if age >= 100:
# 		print("You're already at least 100!")
# 		break
# 	turn100 = (100 - age) + current_year
# 	print(name+" turns 100 years old in the year",turn100,".")

while True:
	name = input("Enter your name.  Type \"stop\" to end: ")
	if (name == "stop"):
		break
	age = int(input("Enter your age: "))
	if age >= 100:
		print("You're already at least 100!")
		break
	turn100 = (100 - age) + current_year
	print(name+" turns 100 years old in the year",turn100,".")