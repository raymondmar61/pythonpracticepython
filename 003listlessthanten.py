a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for eacha in a:
	if eacha < 5:
		print(eacha)

#sample solution includes extra #1 and extra #3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# num = int(raw_input("Choose a number: "))
# new_list = []
# for i in a:
# 	if i < num:
# 		new_list.append(i)
# print(new_list)

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# smaller = int(input("Enter a number less than 90 to return numbers smaller "))
# b = []
# for eacha in a:
# 	if eacha < smaller:
# 		b.append(eacha)
# print(b)

#the one line extra #2 using Filter and Lambda
# n = int(input("Enter a number :"))
# l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print(list(filter((lambda x : x < n),l)))