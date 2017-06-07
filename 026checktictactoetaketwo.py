#Practice Python 026 Check Tic Tac Toe
#Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won assume that in every board there will only be one winner.

gamedemo = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
print(gamedemo[0]) #print [1, 2, 0]
print(gamedemo[-1]) #print [2, 1, 1]
print(gamedemo[0][0]) #print 1
print(gamedemo[1][0]) #print 2

#tictactoeboard = [[a1,b1,c1], [a2,b2,c2], [a3,b3,c3]]
#tictactoeboard = [[00,01,02], [10,11,12], [20,21,22]]

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(game)
playerturn = 1
while True:
	if playerturn % 2 == 0:
		player = 2
		row = int(input("Player 2 enter row coordinate 1-3: "))
		column = int(input("Player 2 enter column coordinate 1-3: "))
	else:
		player = 1
		row = int(input("Player 1 enter row coordinate 1-3: "))
		column = int(input("Player 1 enter column coordinate 1-3: "))
	# player = int(input("Who's turn 1 or 2?  1 goes first:  "))
	# row = int(input("Enter row coordinate 1-3: "))
	# column = int(input("Enter column coordinate 1-3: "))
	if row == 0 or column == 0:
		break
	game[row-1][column-1] = player
	print(game)
	if (game[0] == [1, 1, 1] or game[0] == [2, 2, 2]) or (game[1] == [1, 1, 1] or game[1] == [2, 2, 2])  or (game[2] == [1, 1, 1] or game[2] == [2, 2, 2]) :
		print(player, "horizontal or row win")
		break
	elif ((game[0][0] and game[1][1] and game[2][2] == 1 or game[0][0] and game[1][1] and game[2][2] == 2) or (game[0][2] and game[1][1] and game[2][2] == 1 or game[0][2] and game[1][1] and game[2][2] == 2)):
		print(player, "diagonal win")
		break
	elif ((game[0][0] and game[1][0] and game[2][0] == 1 or game[0][0] and game[1][0] and game[2][0] == 2) or (game[0][1] and game[1][1] and game[2][1] == 1 or game[0][1] and game[1][1] and game[2][1] == 2) or (game[0][2] and game[1][2] and game[2][2] == 1 or game[0][2] and game[1][2] and game[2][2] == 2)):
		print(player, "vertical or column win")
		break
	playerturn += 1

# game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(game)
# game[0][2] = 2
# print(game)
# game[1][2] = 2
# game[2][2] = 2
# print(game)
# if (game[0] == [1, 1, 1] or game[0] == [2, 2, 2]) or (game[1] == [1, 1, 1] or game[1] == [2, 2, 2])  or (game[2] == [1, 1, 1] or game[2] == [2, 2, 2]) :
# 	print("horizontal or row win")
# elif ((game[0][0] and game[1][1] and game[2][2] == 1 or game[0][0] and game[1][1] and game[2][2] == 2) or (game[0][2] and game[1][1] and game[2][2] == 1 or game[0][2] and game[1][1] and game[2][2] == 2)):
# 	print("diagonal win")
# elif ((game[0][0] and game[1][0] and game[2][0] == 1 or game[0][0] and game[1][0] and game[2][0] == 2) or (game[0][1] and game[1][1] and game[2][1] == 1 or game[0][1] and game[1][1] and game[2][1] == 2) or (game[0][2] and game[1][2] and game[2][2] == 1 or game[0][2] and game[1][2] and game[2][2] == 2)):
# 	print("vertical or column win")

# for eachnumber in range(0,3):
# 	for eachnumber2 in range(0,3): 
# 		if ((game[eachnumber][eachnumber2] == 1 & game[eachnumber][eachnumber2] == 1 & game[eachnumber][eachnumber2] == 1) | (game[eachnumber][eachnumber2] == 2 & game[eachnumber][eachnumber2] == 2 & game[eachnumber][eachnumber2] == 2)):
# 			print("test", eachnumber, eachnumber2)

# if ((game[0][1] == 1 & game[1][1] == 1 & game[2][1] == 1) | (game[0][1] == 2 & game[1][1] == 2 & game[2][1] == 2)):
# 	print("test")

# for eachnumber in range(0,3):
# 	for eachnumber2 in range(0,3):
# 		if game[eachnumber][eachnumber2] == 1:
# 			print("test")