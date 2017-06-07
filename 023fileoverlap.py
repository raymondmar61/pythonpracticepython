numbers1 = []
with open("numbers1.txt","r") as num1:
	readnum1 = num1.readlines()
	print(readnum1)
	for eachreadnum1 in readnum1:
		eachreadnum1 = eachreadnum1.strip()			
		numbers1.append(eachreadnum1)	
	#convert string to integer in a list
	numbers1 = list(map(int, numbers1))
	print(numbers1)

numbers2 = []
with open("numbers2.txt","r") as num2:
	readnum2 = num2.readlines()
	print(readnum2)
	for eachreadnum2 in readnum2:
		eachreadnum2 = eachreadnum2.strip()			
		numbers2.append(eachreadnum2)
	#convert string to integer in a list
	numbers2 = list(map(int, numbers2))
	print(numbers2)

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet, add it to both list output and set seen.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
print(numbers1)
print(numbers2)

a = numbers1
b = numbers2

if len(a) >= len (b):
	for eachnumber in range(0,len(a)):
 		if a[eachnumber] in b:
 			print(a[eachnumber])
else:
	for eachnumber in range(0,len(b)):
 		if b[eachnumber] in a:
 			print(b[eachnumber])
#correct answers are 9 and 10

# noduplicates = []
# for eachnumbers1 in numbers1:
# 	for eachnumbers2 in numbers2:	
# 		if eachnumbers1 == eachnumbers2 and eachnumbers1 not in noduplicates:
# 			noduplicates.append(numbers1)
# print(noduplicates)

#error.  Use .readlines() instead of .read()
# numbers2 = []
# with open("numbers2.txt","r") as num2:
# 	readnum2 = num2.read()
# 	print(readnum2)
# 	for eachreadnum2 in readnum2:
# 		eachreadnum2 = eachreadnum2.rstrip()		
# 		numbers2.append(eachreadnum2)
# 	print(numbers2)

#sample solution The solution without functions using a for loop
# primeslist = []
# with open('primenumbers.txt') as primesfile:
# line = primesfile.readline()
# 	while line:
# 		happieslist.append(int(line))
# 		line = happiesfile.readline()
# happieslist = []
# with open('happynumbers.txt') as happiesfile:
# 	line = happiesfile.readline()
# 	while line:
# 		happieslist.append(int(line))
# 		line = happiesfile.readline()
# overlaplist = []
# for elem in primeslist:
# 	if elem in happieslist:
# 		overlaplist.append(elem)
# print(overlaplist)

#sample solution with functions using list comprehensions
# def filetolistofints(filename):
# 	list_to_return = []
# 	with open(filename) as f:
# 		line = f.readline()
# 		while line:
# 			list_to_return.append(int(line))
# 			line = f.readline()
# 	return list_to_return
# primeslist = filetolistofints('primenumbers.txt')
# happieslist = filetolistofints('happynumbers.txt')
# overlaplist = [elem for elem in primeslist if elem in happieslist]
# print(overlaplist)