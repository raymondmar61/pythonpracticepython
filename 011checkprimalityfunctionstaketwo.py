#Practice Python 011 Check Primality Functions
#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).  Add exercise description 051717.

# isprimenumber = 4
# if isprimenumber == 2 or isprimenumber == 3:
# 	print("is a prime number")	
# elif isprimenumber % 2 == 0: 
# 	print("is not a prime number")
# elif isprimenumber % 3 == 0:
# 	print("is not a prime number")
# else:
# 	print("is a prime number")

# for eachnumber in range(1,24):
# 	if eachnumber == 2 or eachnumber == 3:
# 		print(eachnumber, "is a prime number")		
# 	elif eachnumber % 2 == 0: 
# 		print(eachnumber, "is not a prime number")
# 	elif eachnumber % 3 == 0:
# 		print(eachnumber, "is not a prime number")
# 	else:
# 		print(eachnumber, "is a prime number")

def primenumber(inputnumber):
	if inputnumber == 2 or inputnumber == 3:
		print(inputnumber,"is a prime number")	
	elif inputnumber % 2 == 0: 
		print(inputnumber,"is not a prime number")
	elif inputnumber % 3 == 0:
		print(inputnumber,"is not a prime number")
	else:
		print(inputnumber,"is a prime number")
primenumber(int(input("Enter an integer to check if its a prime number: ")))