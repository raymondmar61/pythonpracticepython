userinput = input("Enter three numbers separated by a space: ")
print(userinput)
numbers = userinput.split(" ")
print(numbers) #splitting a string creates a list
number1 = numbers[0]
number2 = numbers[1]
number3 = numbers[2]
print(number1)
print(number2)
print(number3)
a = int(number1)
b = int(number2)
c = int(number3)

def whatislargest(a = 0, b = 0, c = 0):
	"""return largest integer from three inputs"""
	if a > b:
		if a > c:
			print(a, "Variable a is the largest")
		else:
			print(c, "Variable c is the largest")
	elif b > c:
		print(b, "Variable b is the largest")
	else:
		print(c, "Variable c is the largest")
whatislargest(a,b,c)

#sample solutions
# def max_of_three(a,b,c):
# 	max_3=0
# 	if a>b:
# 		#max_3=a
# 		if a>c:
# 			max_3=c
# 		else:
# 			max_3=a
# 	else:
# 		if b>c:
# 			max_3=b
# 		else:
# 			max_3=c
# 	return max_3

# a = input("First number .: ")
# b = input("Second number .: ")
# c = input("Third Number.: ")
# e = (a,b,c)
# h = sorted(e)
# y = len(h) ‐ 1
# print(h[y])