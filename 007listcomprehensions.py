a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
aevennumbers = []
for eacha in a:
	if eacha % 2 == 0:
		aevennumbers.append(eacha)
print(aevennumbers)

b = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
bevennumbers = []
[bevennumbers.append(eachb) for eachb in b if eachb % 2 == 0]
print(bevennumbers)

#one line solution below a list was created as the answer
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([i for i in a if i % 2 == 0])

#sample solution
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [number for number in a if number % 2 == 0]
# print(b)