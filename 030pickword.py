#Practice Python 030 Pick Word

#write a function that picks a random word from a list of words from the SOWPODS dictionary.

import random
# testlist = ["a","b"]
# print(random.choice(testlist))

pickawordlist = []
with open("sowpods.txt","r") as open_file:
	all_text = open_file.read()
	pickawordlist = all_text.split() #.split() takes a string converts to a list
print(random.choice(pickawordlist))

#one solution below
# import random
# with open('sowpods.txt', 'r') as f:
# 	lines = f.readlines()
# print (random.choice(lines).strip())

#official solution
# # import the random library
# import random
# # read all the list of words
# words = []
# with open('sowpods.txt', 'r') as f:
# 	line = f.readline().strip()
# 	words.append(line)
# 	while line:
# 		line = f.readline().strip()
# 		words.append(line)
# # generate a random number
# random_index = random.randint(0, len(words))
# # take the word
# print("Random word: ", words[random_index])