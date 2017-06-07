def getnumber(inputtext):
	return int(input(inputtext))

isitprime = getnumber("Enter a number ")
divisiblenumbers = []
for x in range(1,isitprime+1):
	if isitprime % x == 0:
		divisiblenumbers.append(x)
print(divisiblenumbers)
if len(divisiblenumbers) == 2:
	print(isitprime, "is a prime number")
else:
	print(isitprime, "is not a prime number")

#sample solution
# num = int(raw_input('Insert a number: '))
# a = [x for x in range(2, num) if num % x == 0]
# def is_prime(n):
# 	if num > 1:
# 		if len(a) == 0:
# 			print 'prime'
# 		else:
# 			print 'NOT prime'
# 	else:
# 		print 'NOT prime'
# is_prime(num)

#Functions
# def getinteger():
# 	return int(input("Give me a number: "))
# #What I have done here is called the function (told it to run) by writing age = get_integer(). When this line of code runs, what happens is the program will execute (run) the function by asking me for a number, then returning it (giving it back to me) by saving it inside the variable age. Now when I want to ask the user for another number (this time representing the school year), I do the same thing with the variable school_year.
# age = getinteger()
# schoolyear = getinteger()
# print(age)
# print(schoolyear)
# if age > 15:
# 	print("You are over the age of 15.")
# print("You are in grade " + str(schoolyear))

# def getinteger2(text):
# 	return int(input(text))
# #What if I want to print a different string every time I ask the user for a number, but otherwise use the same idea for the function? In other words, I want a variable parameter in my function that changes every time I call the function based on something I (the programmer) want to be different. I can do this by passing (giving) my function a variable.
# age = getinteger2("Tell me your age: ")
# schoolyear = getinteger2("What grade are you in? ")
# print(age)
# print(schoolyear)
# if age > 15:
# 	print("You are over the age of 15.")
# print("You are in grade " + str(schoolyear))