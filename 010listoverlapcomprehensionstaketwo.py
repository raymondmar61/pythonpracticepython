#Practice Python 010 List Overlap Comprehensions
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.  Add exercise description 051717.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonelementsbetweenlists = [eacha for eacha in a for eachb in b if eacha == eachb]
print(commonelementsbetweenlists)

import random
# randoma = random.sample(range(100),10)
# randomnumber = random.randint(1,20)
# print(randomnumber)
# randomb = random.sample(range(100),randomnumber)
# print(randoma)
# print(randomb)
# commonelementsbetweenlists2 = [eacha for eacha in randoma for eachb in randomb if eacha == eachb]
# print(commonelementsbetweenlists2)

# countlength = 0
# while countlength >= 4:
# 	randoma = random.sample(range(100),10)
# 	randomnumber = random.randint(1,20)
# 	print(randomnumber)
# 	randomb = random.sample(range(100),randomnumber)
# 	print(randoma)
# 	print(randomb)
# 	commonelementsbetweenlists2 = [eacha for eacha in randoma for eachb in randomb if eacha == eachb]
# 	print(commonelementsbetweenlists2)
# 	#print(len(commonelementsbetweenlists2))
# 	countlength = len(commonelementsbetweenlists2)
# 	print(countlength)

# countlength = 0
# while True:
# 	randoma = random.sample(range(100),10)
# 	randomnumber = random.randint(1,20)
# 	print(randomnumber)
# 	randomb = random.sample(range(100),randomnumber)
# 	print(randoma)
# 	print(randomb)
# 	commonelementsbetweenlists2 = [eacha for eacha in randoma for eachb in randomb if eacha == eachb]
# 	countlength = len(commonelementsbetweenlists2)
# 	if countlength >= 4:
# 		break
# print(commonelementsbetweenlists2)

countlength = 0
while True:
	randoma = random.sample(range(100),10)	
	randomb = random.sample(range(100),random.randint(1,20))
	print(randoma)
	print(randomb)
	commonelementsbetweenlists2 = [eacha for eacha in randoma for eachb in randomb if eacha == eachb]	
	countlength = len(commonelementsbetweenlists2)
	if countlength >= 4:
		break
print(commonelementsbetweenlists2)

