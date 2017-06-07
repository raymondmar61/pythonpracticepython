c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

noduplicates = []
for eachc in c:
	for eachd in d:	
		if eachc == eachd and eachc not in noduplicates:
			noduplicates.append(eachc)
print(noduplicates)

#list comprehension
x = [1, 2, 3]
y = [5, 10, 15]
allproducts = [a*b for a in x for b in y]
print(allproducts) #returns [5, 10, 15, 10, 20, 30, 15, 30, 45] You can put multiple for loops inside the comprehension.

#you can also add more complicated conditionals
x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if (a*b)%2 != 0]
print(customlist) #returns [5, 15, 15, 45] the odd products

#In general, the list comprehension takes the form: [EXPRESSION FOR_LOOPS CONDITIONALS]

#to generate a random list, a = random.sample(range(100), 5) for which the list contains five numbers from 0 to 99
# import random
# randomlist = random.sample(range(100), 5)
# print(randomlist)

#As a few commenters / readers of this blog have pointed out (thanks mainly to Gautam and Jeff), the exercise as posed is actually impossible to write in a single line of Python. The problem is this: the proposed reader solution (and the solution that I had in mind myself) as written above does not take into account the fact that there might be  duplicates in the resulting list, where I specifically asked to not include duplicates. This  means that in the simple example I gave above, a’s first element is 1 will be added to the  result list because it is in b. But then it’s next element is also 1, and is also in b, so will be added to the result list. So the solution as given (the comprehension [i for i in a if i in b]) will not yield the correct result on the example solution.