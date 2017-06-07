#Practice Python 024 Draw A Game Board

#Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

gameboardsize = int(input("Enter a game board size: "))
print(gameboardsize)

# correct below with for loop
# for eachboard in range(1,gameboardsize+1):
# 	print(" --- "*gameboardsize)
# 	print("     "*gameboardsize)
# 	print("|   |"*gameboardsize)
# 	print("     "*gameboardsize)
# print(" --- "*gameboardsize)

#correct below with while loop
counter = 0
while gameboardsize != counter:
	print(" --- "*gameboardsize)
	print("     "*gameboardsize)
	print("|   |"*gameboardsize)
	print("     "*gameboardsize)
	counter += 1
print(" --- "*gameboardsize)
