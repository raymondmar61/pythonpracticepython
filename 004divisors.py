number = int(input("Enter a number "))
divisiblenumbers = []
for x in range(1,number+1):
	if number % x == 0:
		divisiblenumbers.append(x)
print(divisiblenumbers)		
#I replaced "eachnumber" with "x" because the code I initially wrote confused me

#sample solution
# num = int(input("Please choose a number to divide: "))
# listRange = list(range(1,num+1))
# divisorList = []
# for number in listRange:
# if num % number == 0:
# divisorList.append(number)
# print(divisorList)

#showoff
# number = input('Please input a number to find its divisors!:')
# number = int(number)
# divisors = [i for i in range(1, number + 1) if number % i == 0]
# print('The divisors are: ' + ', '.join((str(divisor) for divisor in divisors)))