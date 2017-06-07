#Practice Python 003 List Less Than Ten
#list numbers elements if conditional
#write a program that prints out all the elements of the list that are less than 5.  Add exercise description 051717.

# xlist = []
# xlist.append(3)
# print(xlist) #print [3]
# for eachelement in xlist:
# 	print(eachelement) #print 3
# print(len(xlist)) #print 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for eacha in a:
	if eacha < 5:
		print(eacha)

alessthan5 = []
for eacha in a:
	if eacha < 5:
		alessthan5.append(eacha)
print(alessthan5)

ausernumber = []
usernumber = 24
for eacha in a:
	if eacha < usernumber:
		ausernumber.append(eacha)
print(ausernumber)
