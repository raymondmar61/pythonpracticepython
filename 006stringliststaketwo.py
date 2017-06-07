#Practice Python 006 String Lists
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)  Add exercise description 051717.

# userword = "pop"
# userwordbackwards = userword[::-1]
# print(userword)
# print(userwordbackwards)
# if (userword == userwordbackwards):
# 	print(userword+ " is a palindrome. "+userwordbackwards)
# else:
# 	print(userword+ " is not a palindrome. "+userwordbackwards)

userwordinput = input("Enter a string or word(s): ")
userwordinputbackwards = userwordinput[::-1]
if (userwordinput == userwordinputbackwards):
	print(userwordinput+ " is a palindrome: "+userwordinputbackwards)
else:
	print(userwordinput+ " is not a palindrome: "+userwordinputbackwards)