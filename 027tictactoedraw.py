# place = input("Enter row 0-2,column 0-2 (row comma column no spaces in between) ")
# print(place)
# coordinates = place.split(",")
# print(coordinates)
# row = coordinates[0]
# column = coordinates[1]
# print(row)
# print(column)
# gameboard = [["n","n","n"],["n","n","n"],["n","n","n"]]
# print(gameboard)
# gameboard[int(row)][int(column)] = "x"
# print(gameboard)

# count = 1
# gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]
# while count <=9:
# 	if count % 2 != 0:
# 		player1 = input("Player 1 enter row 1-3,column 1-3 (row comma column no spaces in between) ")
# 		coordinates = player1.split(",")
# 		row = coordinates[0]
# 		column = coordinates[1]
# 		gameboard[int(row) - 1][int(column) - 1] = "x"
# 		print(gameboard)	
# 	elif count % 2 == 0:
# 		player2 = input("Player 2e nter row 1-3,column 1-3 (row comma column no spaces in between) ")
# 		coordinates = player2.split(",")
# 		row = coordinates[0]
# 		column = coordinates[1]
# 		gameboard[int(row) - 1][int(column) - 1] = "o"
# 		print(gameboard)
# 	count = count + 1

count = 1
gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]
while count <=9:
	if count % 2 != 0:
		player1 = input("Player 1 enter row 1-3,column 1-3 (row comma column no spaces in between) ")
		coordinates = player1.split(",")
		row = coordinates[0]
		column = coordinates[1]
		if (gameboard[int(row) - 1][int(column) - 1] == "x") or (gameboard[int(row) - 1][int(column) - 1] == "o"):
				print("Space is taken")
				continue
		else:
			gameboard[int(row) - 1][int(column) - 1] = "x"
		print(gameboard)	
	elif count % 2 == 0:
		player2 = input("Player 2 enter row 1-3,column 1-3 (row comma column no spaces in between) ")
		coordinates = player2.split(",")
		row = coordinates[0]
		column = coordinates[1]
		if (gameboard[int(row) - 1][int(column) - 1] == "x") or (gameboard[int(row) - 1][int(column) - 1] == "o"):
				print("Space is taken")
				continue
		else:
			gameboard[int(row) - 1][int(column) - 1] = "o"
		print(gameboard)
	count = count + 1

