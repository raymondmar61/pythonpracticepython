a = [5, 10, 15, 20, 25]
b = []
b.append(a[0])
b.append(a[-1])
print(b)

#sample solution
# def list_ends(a):
# 	return [a[0], a[len(a)‐1]]

#another solution creating a list d without predefining d = [].  Also defining list c calling the function firstlast(c) and in def firstlast(c)
c = [10, 20, 30, 40, 50]
def firstlast(c):
	d = [c[0], c[-1]]
	print(d)
firstlast(c)