#Practice Python 004 Divisors
#list numbers if conditional user input
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)  Add exercise description 051717.

# x = range(2,11)
# for eachx in x:
# 	print(eachx)

answerlist = []
usernumber = 26
x = range(1,usernumber+1)
for eachx in x:
	if (usernumber % eachx == 0):
		answerlist.append(eachx)
print(answerlist)

