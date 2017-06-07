#Practice Python 015 Reverse Word Order
#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
#For example, say I type the string:
#My name is Michele
#Then I would see the string:
#Michele is name My
#shown back to me.   Add exercise description 051717.

# word = "My name is Michelle"
# wordbackward = []
# for eachword in word:
# 	wordbackward.append(eachword)
# print(wordbackward) #print ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'M', 'i', 'c', 'h', 'e', 'l', 'l', 'e'].  #Isn't each word; it's each letter.

word = "My name is Michelle"
wordsplit = word.split() #If you do not include any character, it means “split on all whitespace”.  Another example is word.split("e")
print(wordsplit) #print ['My', 'name', 'is', 'Michelle']
wordjoin = "**".join(word)
print(wordjoin) #print M**y** **n**a**m**e** **i**s** **M**i**c**h**e**l**l**e
listofstrings = ['a', 'b', 'c']
result = "**".join(listofstrings)  
print(result) #print a**b**c

word = "ABC XYZ"
wordsplit = word.split()
print(wordsplit) #print ['ABC', 'XYZ']
print(wordsplit[::-1]) #print ['XYZ', 'ABC']
wordfinal = wordsplit[::-1]
print(wordfinal) #print ['XYZ', 'ABC']
wordjoin = " ".join(wordfinal)
print(wordjoin) #print XYZ ABC

def reversewordorder(longstring="reverse is Default"):
	longstringsplit = longstring.split(" ")
	longstringreverse = longstringsplit[::-1]
	longstringjoin = " ".join(longstringreverse)
	return longstringjoin
print(reversewordorder("My name is Michelle"))
print(reversewordorder("Peter Paul Mary"))
print(reversewordorder("John Paul George Ringo"))

