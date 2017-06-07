#Practice Python 020 Element Search
#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean. Add exercise description 051717

# numberlist = [1, 3, 4, 5, 9, 35]
# userguess = 10
# count = 0
# while count != len(numberlist)+1:
# 	if count == len(numberlist):
# 		print(userguess,"is not in the number list")
# 		break
# 	elif userguess == numberlist[count]:
# 		print(userguess,"is in the number list")
# 		break			
# 	count +=1

def numberlistsearch(userguess, numberlist):
	count = 0
	while count != len(numberlist)+1: #bad programming
		if count == len(numberlist):
			print(userguess,"is not in the number list")
			break
		elif userguess == numberlist[count]:
			print(userguess,"is in the number list")
			break			
		count +=1
numberlistsearch(5,[1, 3, 4, 5, 9, 35])
numberlistsearch(36,[1, 3, 4, 5, 9, 35])
numberlistsearch(96,[45,1, 3, 4, 5, 9, 35])

import math
a = [1, 3, 5, 30, 42, 43, 500]
aguess = 100
halfwaya = math.ceil(len(a) / 2)
if aguess == a[halfwaya]:
	print("Guess is correct")
elif aguess >= a[halfwaya]:
	a = a[halfwaya:]
elif aguess <= a[halfwaya]:
	a = a[:halfwaya]
numberlistsearch(aguess, a)

import random
randomnumberlist = []
randomcount = random.randint(5,21)
for eachrandomcount in range(1,randomcount):	
	randomnumberlistnumber = random.randint(0,100)
	randomnumberlist.append(randomnumberlistnumber)
print(randomnumberlist)
randomnumberlistsorted = sorted(randomnumberlist)
print(randomnumberlistsorted)
numberlistsearch(96,randomnumberlistsorted)

# numberlist = [1, 3, 4, 5, 9, 35]
# userguess = 4
# for eachnumberlist in numberlist:
# 	if userguess == eachnumberlist:
# 		print(userguess,"is in the number list")