#Practice Python 023 File Overlap

#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.  Text files are numbers1.txt and numbers2.txt.

with open("numbers1.txt","r") as open_file:
	numbers1text = open_file.read()
	numbers1textsplit = numbers1text.split()
print(numbers1text) #print numbers1text file on the display
print(numbers1textsplit) #print ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '100']
with open("numbers2.txt","r") as open_file:
	numbers2text = open_file.read()
	numbers2textsplit = numbers2text.split()
print(numbers2text) #print numbers2text file on the display
print(numbers2textsplit) #print ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
seta = set(numbers1textsplit)
setb = set(numbers2textsplit)
print(seta)
print(setb)
print(seta.intersection(setb)) #print {'10', '9'}
