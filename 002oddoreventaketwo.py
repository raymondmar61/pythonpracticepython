#Practice Python 002 Odd Or Even
#input if types int equality comparison numbers mod
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.  Add exercise description 051717.

# number = int(input("Enter a number "))
# print(number)
# if (number % 2 == 0):
# 	print(number,"is an even number.")
# else:
# 	print(number,"is an odd number.")

number = ""
while True:
	number = int(input("Enter a number.  Enter 0 to quit. "))	
	if (number == 0):
		break
	elif (number % 4 == 0):
		print(number,"is an even number and a multiple of 4.")
	elif (number % 2 == 0):
		print(number,"is an even number.")
	else:
		print(number,"is an odd number.")

number2 = int(input("Enter a number. "))
check2 = int(input("Enter a number to divide. "))
if (number2 % check2 == 0):
	print(number2,"is divisible by",check2,"evenly.")
else:
	print(number2,"is not divisible by",check2,"evenly.")