#Practice Python 031 Guess Letters
#Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word.
#As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
#Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining we will deal with those in a future exercise.

# same1list = ['E', 'V', 'A', 'P', 'O', 'R', 'A', 'T', 'E']
# same2list = ['E', 'V', 'A', 'P', 'O', 'R', 'A', 'T', 'E']
# if same1list == same2list:
# 	print("It works")

word = "EVAPORATE"
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
while wordlist != correctguesslist:
	letter = input("Guess your letter ").upper()
	allguesseslist.append(letter)
	if letter in correctguesslist or letter in incorrectguesslist:
		allletters = ", ".join(allguesseslist)
		print("You guessed the letter.  All guesses: "+ allletters)
	elif letter not in wordlist:
		incorrectguesslist.append(letter)
		incorrectletters = ", ".join(incorrectguesslist)
		print("Incorrect guesses: "+ incorrectletters)
	else:
		for wordlistindex in range(0,len(wordlist)):
			if letter == wordlist[wordlistindex]:
				correctguesslist[wordlistindex] = letter
	print(correctguesslist)
print("Total guesses",len(allguesseslist))

#official solution
# if __name__ == '__main__':
# 	print("Welcome to hangman!!")
# 	word = "EVAPORATE"
# 	guessed = "_" * len(word)
# 	word = list(word)
# 	guessed = list(guessed)
# 	lstGuessed = []
# 	letter = input("guess letter: ")
# 	while True:
# 		if letter.upper() in lstGuessed:
# 			letter = ''
# 			print("Already guessed!!")
# 	elif letter.upper() in word:
# 			index = word.index(letter.upper())
# 			guessed[index] = letter.upper()
# 			word[index] = '_'
# 	else:
# 		print(''.join(guessed))
# 		if letter is not '':
# 			lstGuessed.append(letter.upper())
# 		letter = input("guess letter: ")
# 	if '_' not in guessed:
# 		print("You won!!")
# 		break
# #The only thing I would change here is on line 9, change lstGuessed to a set(), so that on line 12, the in check will be very fast.