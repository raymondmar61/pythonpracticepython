#Practice Python 027 Tic Tac Toe Draw
#Ask the user to enter coordinates in the form “row,col” a number, then a comma, then a number.
#Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.  
#RM: I checked whether someone won the game.  I didn't check if a piece is already placed 051917 at 1241hrs.  How about a for loop range to populate a list of possible values.  Each player's input removes a value from the list.  As long as the list has the input, player's input goes through.  If the player's input is not on the list, player must reinput.
#RM:  Added check if a piece is already placed 051917 at 1548

#tictactoeboard = [[a1,b1,c1], [a2,b2,c2], [a3,b3,c3]]
#tictactoeboard = [[00,01,02], [10,11,12], [20,21,22]]
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(game)

# error in vertical or column win and added no player input repeat below
# playerturn = 1
# while True:
# 	if playerturn % 2 == 0:
# 		player = 2
# 		playerinput = input("Player 2 place your 2 in \"row,column\" format no spaces ")
# 	else:
# 		player = 1
# 		playerinput = input("Player 1 place your 1 in \"row,column\" format no spaces ")	
# 	playerlist = playerinput.split(",")
# 	row = int(playerlist[0])	
# 	column = int(playerlist[1])
# 	if row == 0 or column == 0:
# 		break
# 	game[row-1][column-1] = player
# 	print(game)
# 	if (game[0] == [1, 1, 1] or game[0] == [2, 2, 2]) or (game[1] == [1, 1, 1] or game[1] == [2, 2, 2])  or (game[2] == [1, 1, 1] or game[2] == [2, 2, 2]) :
# 		print(player, "horizontal or row win")
# 		break
# 	elif ((game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][0]  == 2 and game[1][1]  == 2 and game[2][2] == 2) or (game[0][2] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][2] == 2 and game[1][1] == 2 and game[2][2] == 2)):
# 		print(player, "diagonal win")
# 		break
# 	elif ((game[0][0] and game[1][0] and game[2][0] == 1) or (game[0][0] and game[1][0] and game[2][0] == 2) or (game[0][1] and game[1][1] and game[2][1] == 1) or (game[0][1] and game[1][1] and game[2][1] == 2) or (game[0][2] and game[1][2] and game[2][2] == 1) or (game[0][2] and game[1][2] and game[2][2] == 2)):
# 		print(player, "vertical or column win")
# 		break
# 	playerturn += 1

tictactoeentrieslist = []
playerturn = 1
while True:
	if playerturn % 2 == 0:
		player = 2
		playerinput = input("Player 2 place your 2 in \"row,column\" format no spaces ")
	else:
		player = 1
		playerinput = input("Player 1 place your 1 in \"row,column\" format no spaces ")
	if playerinput in tictactoeentrieslist:
		playerinput = input("Already occupied.  Re-enter your piece in \"row,column\" format no spaces ")
	playerlist = playerinput.split(",")
	tictactoeentrieslist.append(playerinput)
	row = int(playerlist[0])	
	column = int(playerlist[1])
	if row == 0 or column == 0:
		break
	game[row-1][column-1] = player
	print(game)
	if (game[0] == [1, 1, 1] or game[0] == [2, 2, 2]) or (game[1] == [1, 1, 1] or game[1] == [2, 2, 2])  or (game[2] == [1, 1, 1] or game[2] == [2, 2, 2]) :
		print(player, "horizontal or row win")
		break
	elif ((game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][0]  == 2 and game[1][1]  == 2 and game[2][2] == 2) or (game[0][2] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][2] == 2 and game[1][1] == 2 and game[2][2] == 2)):
		print(player, "diagonal win")
		break
	elif ((game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1) or (game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2) or (game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1) or (game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2) or (game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1) or (game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2)):
		print(player, "vertical or column win")
		break
	playerturn += 1
