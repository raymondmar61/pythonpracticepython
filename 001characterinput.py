from datetime import *
now = datetime.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = ((100 - age) + now.year)
print(name+ " you turn 100 in the year", year)

#sample solution
# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = str((2014 ‐ age)+100)
# print(name + " will be 100 years old in the year " + year)

#extras
# 1.Add on to the previous program by asking the user for another number and  printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# numberofcopies = int(input("How many copies printed "))
# year = ((100 - age) + now.year)
# for eachnumberofcopies in range(0,numberofcopies):
# 	print(name+ " you turn 100 in the year", year, "\n")

# while True:
# 	name = input("Enter your name: ")
# 	if name == "q":
# 		break
# 	age = int(input("Enter your age: "))
# 	year = ((100 - age) + now.year)
# 	print(name+ " you turn 100 in the year", year)
