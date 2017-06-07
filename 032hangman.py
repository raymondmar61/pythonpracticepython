#Practice Python 032 Hangman
#We will finish building Hangman. The player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
#add the following features: Only let the user guess 6 times, and tell the user how many guesses they have left.  Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them let them guess again.
#Optional additions: When the player wins or loses, let them start a new game.  Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging do the other parts of the exercise first!

import random
def hangman():
	pickawordlist = []
	with open("sowpods.txt","r") as open_file:
		all_text = open_file.read()
		pickawordlist = all_text.split()
	word = (random.choice(pickawordlist))
	wordlist = []
	allguesseslist = []
	correctguesslist = []
	incorrectguesslist = []
	print(word)
	for eachword in word:
		wordlist.append(eachword)
		correctguesslist.append("_")
	print(wordlist)
	print(correctguesslist)
	incorrectguesses = 1
	while (wordlist != correctguesslist):
		if incorrectguesses == 7:
			print("Hangman")
			print("The word is " +word)
			break
		letter = input("Guess your letter ").upper()
		allguesseslist.append(letter)
		if letter in correctguesslist or letter in incorrectguesslist:
			allletters = ", ".join(allguesseslist)
			print("You guessed the letter.  All guesses: "+ allletters)
		elif letter not in wordlist:
			incorrectguesslist.append(letter)
			incorrectletters = ", ".join(incorrectguesslist)
			print(incorrectguesses,"Incorrect guesses: "+ incorrectletters)
			incorrectguesses += 1
		else:
			for wordlistindex in range(0,len(wordlist)):
				if letter == wordlist[wordlistindex]:
					correctguesslist[wordlistindex] = letter
		print(correctguesslist)
	print("Total guesses",len(allguesseslist))

playhangman = input("Do you want to play hangman? y or n ")
while playhangman == 'y':
	hangman()
	playhangman = input("Do you want to play hangman again? y or n ")

#solution
# import random
# def choose_random_word():
# 	words=[]
# 	with open('sowpods.txt', 'r') as file:
# 		line = file.readline()
# 		while line:
# 			words.append(line.replace("\n","".strip()))
# 			line = file.readline()
# 	choice=words[random.randint(0,len(words)‐1)]
# 	return choice
# print("Welcome to Hangman!")
# secret_word=choose_random_word()
# dashes=list(secret_word)
# display_list=[]
# for i in dashes:
# 	display_list.append("_")
# count=len(secret_word)
# guesses=0
# letter = 0
# used_list=[]
# while count != 0 and letter != "exit":
# 	print(" ".join(display_list))
# 	letter=input("Guess your letter: ")
# 	if letter.upper() in used_list:
# 		print("Oops! Already guessed that letter.")
# 	else:
# 		for i in range(0,len(secret_word)):
# 			if letter.upper() == secret_word[i]:
# 			display_list[i]=letter.upper()
# 			count ‐= 1
# 		guesses +=1
# 	used_list.append(letter.upper())
# if letter == "exit":
# 	print("Thanks!")
# else:
# 	print(" ".join(display_list))
# 	print("Good job! You figured that the word is "+secret_word+" after guessing %s letters!" % guesses) #this line truncated in solution