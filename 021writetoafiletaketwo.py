#Practice Python 021 Write To A File

#The simplest form of writing to a file is a text file.  The code looks like this:
#with open('file_to_save.txt', 'w') as open_file:
#	open_file.write('A string to write')
#An alternate way of writing the same code is like so:
# open_file = open('file_to_save.txt', 'w')
# open_file.write('A string to write')
# open_file.close()
#The first is considered better programming practice, but the second might explain a little bit better what is going on in the first code sample.
#The second  is considered worse programming practice, because in case there is an error in the program and it terminates before hitting the .close() statement, there will be a floating open file object somewhere in memory. You do this enough times and it becomes a problem, especially for production environments. For playing around with Python, this is not usually a problem, but why not learn how to program correctly the first time?

with open("021writetoafiletaketwo.txt","w") as open_file:
	open_file.write("Hello!")
	open_file.write("How are you doing?  ")
	open_file.write("Today is a good day.")
	open_file.write("Paragraph break \n")
	open_file.write("Am I in a new paragraph?")
