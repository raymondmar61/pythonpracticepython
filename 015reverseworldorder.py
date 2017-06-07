#You can “split” or tear apart strings based on a given set of characters. For example:
teststring = "this is a test"
result = teststring.split("t")
print(result) #['', 'his is a ', 'es', '']

teststring = " this            has a lot         of spaces and      tabs"
result = teststring.split()
print(result) #['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']

#You can also relatively easily “join” strings together.  For example:
listofstrings = ['a', 'b', 'c']
result = "**".join(listofstrings)
print(result) #a**b**c

#remember strings are lists

#trial and error, I had the answer.  The for loop was unnecessary
# longstring = input("Enter something ")
# print(longstring)
# # longstring = list(longstring)
# # print(longstring)
# longstring = longstring.split()
# print(longstring)
# print(len(longstring))
# #length = len(longstring)
# # answer = " ".join(longstring)[::-1]
# # print(answer)
# for length in range(1,len(longstring)):
# 	print(length)
# 	print(longstring[::-length])
# 	answer = " ".join(longstring[::-length])
# 	print(answer)

longstring = input("Enter something ")
print(longstring)
longstring = longstring.split()
print(longstring)
print(longstring[::-1])
answer = " ".join(longstring[::-1])
print(answer)


