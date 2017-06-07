#Practice Python 014 List Remove Duplicates
#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.  Add exercise description 051717.

#Sets.  In mathematics, a set is a collection of elements where no element is repeated. This becomes useful because if you know your data is stored in a set, you are guaranteed to have unique elements.
#In Python, you make and use a set with the set() keyword. For example:
names = set()
names.add("Michele")
names.add("Robin")
names.add("Michele")
print(names) #print {'Robin', 'Michele'}
#You can convert from a list to a set and a set to a list pretty easily:
names = ["Michele", "Robin", "Sara", "Michele"]
names = set(names)
names = list(names)
print(names) #print ['Michele', 'Sara', 'Robin']

#Practice Python 005 List Overlap solution
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# seta = set(a)
# setb = set(b)
# print(seta)
# print(setb)
# print(seta.intersection(setb))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newa = []
for eacha in a:
	if eacha not in newa:
		newa.append(eacha)
print(newa)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newb = []
def uniquelist(numberslist):
	for eachnumberslist in numberslist:
		if eachnumberslist not in newb:
			newb.append(eachnumberslist)
	return newb
print(uniquelist(b))

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(c) 
print(c) #print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
c = list(c)
print(c)  #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


