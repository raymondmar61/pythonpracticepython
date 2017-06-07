#Practice Python 034 Birthday Json

#Modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
#Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

#the toplevel container is a dictionary, with the keys name, shirt_color, laptops, has_a_dog, and items_on_desk.  The keys can be lists, strings, booleans, or other dictionaries.
#{"name":"Raymond","shirt-color":"black", laptops":[{"brand":"HP","os":"Windows 7"},{"brand":"Dell","os":"Windows XP"}],"has_a_dog":false,"items_on_desk":["mug","pen","monitor"]}

#The dictionary info_about_me will be saved to disk.  The variable name will not.  JSON won’t remember the name of the variable you saved your dictionary in.
import json
info_about_me = {"name":"Raymond","has a dog":False}
with open("info.json","w") as f:
	json.dump(info_about_me, f)
#Alternatively, you can also manually create a JSON file and type JSON directly into it.  Just save the file with the .json extension and copy the dictionary directly into the file.

#Now I can use the information about me that I saved to disk in another program (written in a completely different file) to do something like printing a  essage. When I saved the JSON file, the variable name of my dictionary was not saved with it, so when I load the JSON file I need to save it into a variable. I can use the same json library to do this.
import json
with open("info.json","r") as f:
	info = json.load(f)
if info["has a dog"]:
	print("{} has a dog".format(info["name"]))
else:
	print("{} doesn't have a dog".format(info["name"])) #print Raymond doesn't have a dog

#You need to update the output of json.load with a_dict and then dump the result. And you cannot append to the file but you need to overwrite it.  i.e read the dictionary, update the dictionary by rewriting the dictionary with new key and value.  https://stackoverflow.com/questions/18980039/how-to-append-in-a-json-file-in-python
with open("birthdays.json","r") as b:
	birthdaydictionary = json.load(b)
newname = input("Enter another person's name ")
newbirthday = input("Enter person's birthday mm/dd/yyyy ")
print(newname)
print(newbirthday)
addbirthdaydictionary = {}
addbirthdaydictionary[newname] = newbirthday
birthdaydictionary.update(addbirthdaydictionary)
with open("birthdays.json","w") as b2:
	json.dump(birthdaydictionary, b2)

#solution
# import json
# birthday = {}
# with open('birthdays.json', 'r') as f:
# 	birthday = json.load(f)
# def add_entry():
# 	name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
# 	date = input('When is {} born?\n'.format(name))
# 	birthday[name] = date
# 	with open('birthdays.json', 'w') as f:
# 		json.dump(birthday, f)
# 	print('{} was added to my birthday list\n'.format(name))
# def find_date():
# 	name = input("who's birthday do you want to know?\n").title()
# 		try :
# 			if birthday[name]:
# 				print('{} is born on {}\n'.format(name, birthday[name]))
# 		except KeyError:
# 			print('{} is not in the list\n'.format(name))
# def list_entries():
# 	print('The current entries in my birthday list are:\n============================================')
# 	for key in birthday:
# 		print(key.ljust(31), ':', birthday[key])
# 	print()
# while True:
# 	what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
# 	if what_next == 'Quit':
# 		print('Good Bye')
# 		raise SystemExit(0)
# 	elif what_next == 'Add':
# 		add_entry()
# 	elif what_next == 'Find':
# 		find_date()
# 	elif what_next == 'List':
# 		list_entries()