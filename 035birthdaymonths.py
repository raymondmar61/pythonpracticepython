#Practice Python 035 Birthday Months

#load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.  Your program should output something like:  {"May": 3,"November": 2,"December": 1}

from collections import Counter
sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
c = Counter(sandwiches)
print(c)
print("There are {} ham sandwiches".format(c["ham"]))
print("\n")

import datetime
a = "01/02/1953"
datee = datetime.datetime.strptime(a, "%m/%d/%Y") #Y must be capatialized
print(datee.month)
print(datee.year)
print(datee.day)
mydate = datetime.datetime.now()
mydate.strftime("%B")
print(mydate.strftime("%B"))
print("\n")

import json
import datetime
monthscount = []
with open("birthdays.json","r") as r:
	info = json.load(r)
for birthday in info:
	print(info[birthday])
	b = info[birthday]
	datee = datetime.datetime.strptime(b, "%m/%d/%Y")	
	print(datee.strftime("%B")) #%B converts month from number to full spelling
	monthscount.append(datee.strftime("%B"))
	monthscount.sort()
print(monthscount)
m = Counter(monthscount)
print(m)

#solution
# with open("birthdays.json", "r") as f:
# 	birthdays = json.load(f)
# num_to_string = {
# 	1: "January",
# 	2: "February",
# 	3: "March",
# 	4: "April",
# 	5: "May",
# 	6: "June",
# 	7: "July",
# 	8: "August",
# 	9: "September",
# 	10: "October",
# 	11: "November",
# 	12: "December"
# }
# months = []
# for name, birthday_string in birthdays.items():
# 	month = int(birthday_string.split("/")[0])
# 	months.append(num_to_string[month])
# print(Counter(months))