#Practice Python 005 List Overlap
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.  Add exercise description 051717.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# combinedlists = a+b
# print(combinedlists)
# print(set(combinedlists))

seta = set(a)
setb = set(b)
print(seta)
print(setb)
print(seta.intersection(setb))

# import random
# print(random.randrange(0,100))
# randomlista = []
# randomlistb = []
# randomnumbera = ""
# while randomnumbera != 0:
# 	randomnumbera = random.randrange(0,100)
# 	randomnumberb = random.randrange(0,100)
# 	if randomnumbera == 0:
# 		break
# 	randomlista.append(randomnumbera)
# 	randomlistb.append(randomnumberb)
# print(randomlista)
# print(randomlistb)

import random
print(random.randrange(0,100))
randomlista = []
randomnumbera = ""
while randomnumbera != 0:
	randomnumbera = random.randrange(0,100)
	if randomnumbera == 0:
		break
	randomlista.append(randomnumbera)
randomlistb = []
randomnumberb = ""
while randomnumberb != 0:
	randomnumberb = random.randrange(0,100)
	if randomnumberb == 0:
		break
	randomlistb.append(randomnumberb)
print(randomlista)
print(randomlistb)
setrandomlista = set(randomlista)
setrandomlistb = set(randomlistb)
print(setrandomlista.intersection(setrandomlistb))

