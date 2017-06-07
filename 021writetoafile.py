#open() function takes two arguments.  First is the name of a file as a string (if the file does not exist, Python creates it).  Second is an argument that  represents how the file should be opened which are "w" write and "r" read; also "r+" for read write.
#Caution:  opening a file with 'w' when you want to only read it will overwrite the old file.
#To look for files in other directories, use the ../ notation to move up and down directories as necessary.
with open("filename.txt","w") as variablenamehere:
	#inside the code block indented underneath, there will be a variable called "variablenamehere" representing the file object
	#The write() portion is .write() with a string (if something is not a string, turn it into a string first), and it will write to the end of the file.
	variablenamehere.write("Write what you want here")

#you have to convert numbers or objects into strings before you write them to a file.
with open("text.txt","w") as texttest:
	for x in range(0,10):
		texttest.write(str(x))
		texttest.write("\n")
	texttest.write("The range is completed.")

with open("text.xls","w") as excel:
	for x in range(0,10):
		excel.write(str(x))
		excel.write("\n")
	excel.write("okay the numbers printed")