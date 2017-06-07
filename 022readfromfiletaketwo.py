#Practice Python 022 Read From File

#Simply, reading to a file takes two steps:  1. Opening the file for reading  2. Read!
#Opening a file for reading is the same as opening for writing, just using a different flag:
#with open('file_to_read.txt', 'r') as open_file:
#	all_text = open_file.read()
#Another way of reading data from the file is line by line:
# with open('file_to_read.txt', 'r') as open_file:
# 	line = open_file.readline()
# 	while line:
# 		print(line)
# 		line = open_file.readline()

# with open("names.txt","r") as open_file:
# 	all_text = open_file.read()
# print(all_text) #print names.txt file on the display

# with open("names.txt","r") as open_file:
# 	line = open_file.readline()
# 	while line:
# 		print(line) #print names.txt file on the display with a line break \n
# 		line = open_file.readline()

# with open("names.txt","r") as open_file:
# 	Lea = 0
# 	Darth = 0
# 	Luke = 0
# 	line = open_file.readline()
# 	while line:
# 		for eachline in line:
# 			if line == "Lea":
# 				Lea+=1
# 			elif line == "Darth":
# 				Darth+=1
# 			elif line == "Luke":
# 				Luke+=1
# 		line = open_file.readline()
# print(Lea)
# print(Darth)
# print(Luke)

# with open("names.txt","r") as open_file:
# 	line = open_file.readline()
# 	while line:
# 		print(line)
# 		starwarslist = line.split()	
# 		line = open_file.readline()
# print(starwarslist)

with open("names.txt","r") as open_file:
	all_text = open_file.read()
	starwarslist = all_text.split()
print(all_text)
print(starwarslist)
Lea = 0
Darth = 0
Luke = 0
for eachstarwarslist in starwarslist:
	if eachstarwarslist == "Lea":
		Lea += 1
	elif eachstarwarslist == "Darth":
		Darth += 1
	elif eachstarwarslist == "Luke":
		Luke += 1
print("Lea: ",Lea)
print("Darth: ",Darth)
print("Luke: ",Luke)
print("The sum must equal to 100:", Lea + Darth + Luke)

# x = [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2]
# for number in range(1,11):
# 	print("number",number,"in x list:",x.count(number))
# for eachstarwarslistcount in starwarslist:
# 	print("name",eachstarwarslistcount,"in names.txt:",starwarslist.count(eachstarwarslistcount))

from collections import Counter
print(Counter(starwarslist)) #print Counter({'Lea': 54, 'Darth': 31, 'Luke': 15})
