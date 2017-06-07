names = set()
names.add("Michelle")
names.add("Raymond")
names.add("James")
names.add("Michelle")
print(names) # returns {'Raymond', 'James', 'Michelle'}

#You can do to a set almost anything you can do to a list (except ask for things like “the third element”).

#You can convert from a list to a set and a set to a list pretty easily
namesinlist = ["Michele", "Robin", "Sara", "Michele"]
print(namesinlist)
namesinlist = set(namesinlist) 
print(namesinlist) #{'Michele', 'Robin', 'Sara'}
namesinlist = list(namesinlist) 
print(namesinlist) #['Michele', 'Robin', 'Sara']

import random
randomlist = []
for eachnumber in range(1,11):
	randomlist.append(random.randint(1,5))
print(randomlist)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = randomlist
def removeduplicates(duplicatelist):
	duplicatelist = set(duplicatelist)
	duplicatelist = list(duplicatelist)
	print(duplicatelist)
removeduplicates(a)

#samplesolutions
# def dedupe_v1(x):
# 	y = []
# 	for i in x:
# 	if i not in y:
# 		y.append(i)
# 	return y

# def dedupe_v2(x):
# 	return list(set(x))
# a = [1,2,3,4,3,2,1]
# print a
# print dedupe_v1(a)
# print dedupe_v2(a)