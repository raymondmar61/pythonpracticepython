#Practice Python 007 List Comprehensions
#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.  Add exercise description 051717.

allnumbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# evennumbers = []
# for eachallnumbers in allnumbers:
# 	if eachallnumbers % 2 == 0:
# 		evennumbers.append(eachallnumbers)
# print(evennumbers)

print([x for x in allnumbers if x % 2 == 0])