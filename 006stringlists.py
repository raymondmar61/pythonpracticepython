userstring = []
userstring = input("Enter a string ")
forwardstring = (userstring[::1])
backwardstring = (userstring[::-1])
if forwardstring == backwardstring:
	print("The word is a palindrome which reads the same forwards and backwards")
	print(backwardstring)
else:
	print("The word is not a palindrome")

#Because strings are lists, you can do to strings everything that you do to lists. You can iterate through them:
# string = "example"
# for c in string:
# 	print "one letter: " + c
# Will give the result:
# one letter: e
# one letter: x
# one letter: a
# one letter: m
# one letter: p
# one letter: l
# one letter: e
# You can take sublists:
# >>> string = "example"
# >>> s = string[0:5]
# >>> print s
# exam

#sample solution
# wrd=input("Please enter a word")
# wrd=str(wrd)
# rvs=wrd[::‐1]
# print(rvs)
# if wrd == rvs:
# print("This word is a palindrome")
# else:
# print("This word is not a palindrome")