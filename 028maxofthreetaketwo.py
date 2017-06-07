#Practice Python 028 Max Of Three
#Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!  The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

def maxthree(a, b, c):
	if a > b and a > c:
		print(a,"a")
	elif b > a and b > c:
		print(b,"b")
	elif c > a and c > b:
		print(c,"c")
	else:
		print("There is a tie for largest number")
maxthree(3,2,1)