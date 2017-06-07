number = int(input("Enter a number: "))
print(number)
if number % 4 == 0:
	print("Extra #1 You typed an even number divisible by 4")
elif number % 2 == 0:
	print("You typed an even number")
else:
	print("You typed an odd number")

#samplesolution
# num = input("Enter a number: ")
# mod = num % 2
# if mod > 0:
# print("You picked an odd number.")
# else:
# print("You picked an even number.")

# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# check = int(input("Enter a number to check: "))
# divide = int(input("Enter a number to divide: "))
# if check/number % 2 == 0:
# 	print(check, "and" ,divide, "divides evenly")
# else:
# 	print(check, "and" ,divide, "divides oddly")
# 	