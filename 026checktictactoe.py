matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[1,2,3],[1,2,3]]
# print(matrix)
# print(matrix[0]) #[1, 2, 3]
# print(matrix[1])
# print(matrix[2])
# print(matrix[-1])
# print(matrix[0][0]) #1
# print(matrix[1][0]) #4
# print(matrix[2][-1]) #9
# firstlist = matrix[0]
# print(firstlist) #[1, 2, 3]
print(matrix2) #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(matrix2[0][0],matrix2[1][0]) #1 1

tictactoe = [[0,0,2],[0,2,0],[2,0,0]]
# 	print("Winner")
for eachnumber in range(0,3):
	# if (tictactoe[0] == [1, 1, 1]) or (tictactoe[1] == [1, 1, 1]) or (tictactoe[2] == [1, 1, 1]):
	if (tictactoe[eachnumber] == [1, 1, 1] or tictactoe[eachnumber] == [2, 2, 2]):
		print("Winner horizontal")
		break
	# elif (tictactoe[0][0] == 1 and tictactoe[1][0] == 1 and tictactoe[2][0] == 1) or (tictactoe[0][1] == 1 and tictactoe[1][1] == 1 and tictactoe[2][1] == 1) or (tictactoe[0][2] == 1 and tictactoe[1][2] == 1 and tictactoe[2][2] == 1):
	elif ((tictactoe[0][eachnumber] == 1 and tictactoe[1][eachnumber] == 1 and tictactoe[2][eachnumber] == 1)) or ((tictactoe[0][eachnumber] == 2 and tictactoe[1][eachnumber] == 2 and tictactoe[2][eachnumber] == 2)):
		print("Winner vertical")
		break
	elif (tictactoe[0][0] == 1 and tictactoe[1][1] == 1 and tictactoe[2][2] == 1) or (tictactoe[0][-1] == 1 and tictactoe[1][-2] == 1 and tictactoe[2][-3] == 1) or (tictactoe[0][0] == 2 and tictactoe[1][1] == 2 and tictactoe[2][2] == 2) or (tictactoe[0][-1] == 2 and tictactoe[1][-2] == 2 and tictactoe[2][-3] == 2):
		print("Winner diagonally")
		break

#sample solutions
#Not using too many functions, but using the NUMPY library to transpose the game board, turning columnchecking into rowchecking.
# import numpy
# game = [[2,2,1],[1,1,2],[1,2,1]]
# set_r = ()
# set_c = ()
# def line_match(game):
# 	for i in range(3):
# 		set_r = set(game[i])
# 		if len(set_r) == 1 and game[i][0] != 0:
# 			return game[i][0]
# 	return 0
# # transposed column function for future use
# # def column(game):
# # 	trans = numpy.transpose(game)
# # 	for i in range(3):
# # 		set_r = set(trans[i])
# # 		if len(set_r) == 1 and trans[i][0] != 0:
# # 			return list(set_r)[0]
# def diagonal_match(game):
# 	if game[1][1] != 0:
# 		if game[1][1] == game[0][0] == game[2][2]:
# 			return game[1][1]
# 		elif game[1][1] == game[0][2] == game[2][0]:
# 			return game[1][1]
# 	return 0
# if line_match(game) > 0:
# 	print (str(line_match(game)) + str(" row wins!"))
# if line_match(numpy.transpose(game)) > 0:
# 	print (str(line_match(numpy.transpose(game))) + str(" column wins!"))
# if diagonal_match(game) > 0:
# 	print (str(diagonal_match(game)) + str(" diagonal wins!"))

# #Using set()
# def checkGrid(grid):
# 	# rows
# 	for x in range(0,3):
# 		row = set([grid[x][0],grid[x][1],grid[x][2]])
# 		if len(row) == 1 and grid[x][0] != 0:
# 			return grid[x][0]
# 	# columns
# 	for x in range(0,3):
# 		column = set([grid[0][x],grid[1][x],grid[2][x]])
# 		if len(column) == 1 and grid[0][x] != 0:
# 			return grid[0][x]
# 	# diagonals
# 	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
# 	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
# 	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
# 		return grid[1][1]
# 	return 0
# also_no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 0]]
# print(checkGrid(also_no_winner))