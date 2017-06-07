def gameboard(boardsize):
	for eachboardsize in range(0,boardsize):
		print(" -2- " * boardsize)	
		# print("\n" * boardsize)
		print("| 3 |" * boardsize)
	print(" -4- " * boardsize)

boardsize = int(input("Enter boardsize grid square: "))
gameboard(boardsize)

#sample solution
# #Each row consists of horizontal pieces (‐‐‐) and vertical pieces (|). Each of these shows up in a pattern, so we can rely on for loops to help with the rendering.
# #To print a single row, we want to do something like this:
# def print_horiz_line():
# 	print(" ‐‐‐ " * board_size)
# #To print the vertical parts of the row, we want something like this, because we don’t care about trailing whitespace, and because we want one more vertical line than the size of the board:
# def print_vert_line():
# 	print("| " * (board_size + 1))
# if __name__ == "__main__":
# 	board_size = int(input("What size of game board? "))
#  #For a board of size board_size we want to print that many horizontal pieces and vertical pieces, plus an extra horizontal piece for the bottom.
# 	for index in range(board_size):
# 		print_horiz_line()
# 		print_vert_line()
# 	print horiz_line()


# def drawboard(kamal):
# 	kamal = int(kamal)
# 	i = 0
# 	ho = "‐‐‐ "
# 	ve = "| "
# 	ho = ho * kamal
# 	ve = ve * (kamal+1)
# 	while i < kamal+1:
# 		print ho
# 		if not (i == kamal):
# 			print ve
# 	i += 1