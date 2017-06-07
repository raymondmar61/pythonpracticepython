#Practice Python 012 List Ends
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.  Add exercise description 051717.

# a = [5, 10, 15, 20, 25]
# afirstlast = []
# afirstlast.append(a[0])
# afirstlast.append(a[-1])
# print(a[0])
# print(a[-1])
# print(afirstlast)

a = [5, 10, 15, 20, 25]
def firstlastnumbers(numberlist):
	numberlistfirstlast = []
	numberlistfirstlast.append(numberlist[0])
	numberlistfirstlast.append(numberlist[-1])	
	print(numberlistfirstlast)
firstlastnumbers(a) #return [5, 25]

import random
randomcounter = random.randint(2,11)
initialcounter = 0
b = []
while initialcounter != randomcounter:
	b.append(random.randint(1,99))
	initialcounter += 1
print(b)
firstlastnumbers(b)