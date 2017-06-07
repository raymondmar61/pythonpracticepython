a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Function source http://www.dotnetperls.com/duplicates-python
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet, add it to both list output and set seen.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
print(remove_duplicates(a))
print(remove_duplicates(b))

a = remove_duplicates(a)
b = remove_duplicates(b)

if len(a) >= len (b):
	for eachnumber in range(0,len(a)):
 		if a[eachnumber] in b:
 			print(a[eachnumber])
else:
	for eachnumber in range(0,len(b)):
 		if b[eachnumber] in a:
 			print(b[eachnumber])

#Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point we’ll get to it soon)