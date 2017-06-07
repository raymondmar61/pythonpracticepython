# with open("names.txt","r") as starwarsnamestoread:
# 	assignedvariable = starwarsnamestoread.read()
# 	print(assignedvariable)

#another way reading data line by line using while loop which adds a blank line between each line
#Instead of print(line), you can imagine doing anything you want to the line of text… If you save it to a variable, you have a string that you can then use  something like .strip() or .split() with.
# with open("names.txt","r") as starwarsnamestoreadwhileloop:
# 	linevariable = starwarsnamestoreadwhileloop.readline()
# 	while linevariable:
# 		print(linevariable)
# 		linevariable = starwarsnamestoreadwhileloop.readline()

# filename = "names.txt"
# namelist = []
# for eachline in open(filename,"r").readlines():
# 	namelist.append(eachline.rstrip())
# 	namecount = list(set(namelist))
# 	for eachname in namecount:
# 		print(eachname,"occured ", namelist.count(eachname), " times")

#sample solution
filename = "names.txt"
counter_dict = {}
with open(filename) as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()
print(counter_dict)