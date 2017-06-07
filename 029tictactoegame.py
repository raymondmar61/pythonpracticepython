#Practice Python 029 Tic Tac Toe Game
#Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two player game that you can play with a friend.
#You should keep track of who won if there is a winner, show a congratulatory message on the screen. If there are no more moves left, don’t ask for the next player’s move!
#As a bonus, you can ask the players if they want to play again and keep a running tally of who won more Player 1 or Player 2.
#A large part of programming is reusing code written by someone else to accomplish a task. Sometimes it is fun to write a solution yourself, but other times you want to build on top of something else. This exercise gives you an opportunity to practice one of the arts of programming starting from code someone else wrote and creating something on top of it.

def tictactoe():
	game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	print(game)
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
			playgame = input("Do you want to play Tic Tac Toe again?  Type y to play ")
			if playgame == "y":
				tictactoe()
			else:
				break
		elif ((game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][0]  == 2 and game[1][1]  == 2 and game[2][2] == 2) or (game[0][2] == 1 and game[1][1] == 1 and game[2][2] == 1) or (game[0][2] == 2 and game[1][1] == 2 and game[2][2] == 2)):
			print(player, "diagonal win")
			playgame = input("Do you want to play Tic Tac Toe again?  Type y to play ")
			if playgame == "y":
				tictactoe()
			else:
				break
		elif ((game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1) or (game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2) or (game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1) or (game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2) or (game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1) or (game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2)):
			print(player, "vertical or column win")
			playgame = input("Do you want to play Tic Tac Toe again?  Type y to play ")
			if playgame == "y":
				tictactoe()
			else:
				break
		if (game[0][0] != 0 and game[1][0] != 0 and game[2][0] != 0) and (game[0][1] != 0 and game[1][1] != 0 and game[2][1] != 0) and (game[0][2] != 0 and game[1][2] != 0 and game[2][2] != 0):
			print("No more moves.  Game over.")
			break
		playerturn += 1

playgame = input("Do you want to play Tic Tac Toe?  y or n. ")
if playgame == "y":
	tictactoe()
