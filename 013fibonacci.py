#visit https://www.mathsisfun.com/numbers/fibonacci-sequence.html for the rule and grid

# tillN = int(input("Enter Nnmber of Fibonacci you want: "))
# a=0
# b=1
# for i in range(0,tillN+1):
# 	print(a)
# 	a,b=b,a+b

tillN = int(input("Enter Number of Fibonacci you want: "))
a=0
b=1
for i in range(0,tillN+1):
	print(a)
	temp_a = a
	a = b
	b = temp_a + b
#where b is using the old value of a before a was reassigned to the value of b.  Python first evaluates the right-hand expression and stores the results on the stack, then takes those two values and assigns them to a and b. That means that a + b is calculated before a is changed.
#Source: http://stackoverflow.com/questions/21990883/python-a-b-b-a-b

# def fibby():
# 	num = input("Number of Fibonacci numbers you want: ")
# 	a, b = 0, 1
# 	for i in range(int(num)):
# 		a, b = b, a + b
# 		print(a)
# fibby()