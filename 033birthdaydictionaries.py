#Practice Python 033 Birthday Dictionaries

#For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.

#brief review and new concepts for dictionaries
price_dictionary = {"banana": 1.50, "avocado": 0.99, "heirloom tomato": 0.89, "cherry tomato pack": 3.00}
print(price_dictionary["banana"]) #print 1.50
print(price_dictionary.keys()) #print dict_keys["banana", "avocado", "heirloom tomato", "cherry tomato pack"]
price_dictionary["granny smith apple"] = 0.49
print(price_dictionary) #print {'granny smith apple': 0.49, 'heirloom tomato': 0.89, 'cherry tomato pack': 3.0, 'avocado': 0.99, 'banana': 1.5}
price_dictionary["dog food"] = "only at Petco"
print(price_dictionary["dog food"]) #print only at Petco
price_dictionary["dog food"] = 10.33
print(price_dictionary["dog food"]) #print 10.99
print(price_dictionary.get("lemon", "no food like this")) #print no food like this because there is no lemon in price_dictionary
#if we want to check if a particular key is in our dictonary, it is very easy. Just use the in keyword:
print("lemon" in price_dictionary) #print False
print("banana" in price_dictionary) #print True

a = 1
b = 10
#use the .format() method to cast (i.e. transform) your number into a string when it gets printed.
#the variables a and b get converted into strings automatically and injected into our print statement cleanly. You can do this with floats, lists, dictionaries, or anything else you want to display.
print("my number is {} and his number is {}".format(a, b)) #print my number is 1 and his number is 10
print("\n")

birthdays = {"Raymond Mar":"08/03/1974", "Edward Elric":"10/04/2003", "Sissy Speck":"07/18/1982", "Benjamin Franklin":"01/17/1706"}
print("Welcome to the birthday dictionary.  We know the birthdays:")
for eachkey in birthdays:
	print(eachkey, end=", ")
print("")
lookupbirthday = input("Who's birthday do you want to look up? ")
print(lookupbirthday+"'s birthday is "+birthdays[lookupbirthday]+".")

#solution
# if __name__ == '__main__':
# 	birthdays = {'Albert Einstein': '03/14/1879','Benjamin Franklin': '01/17/1706','Ada Lovelace': '12/10/1815','Donald Trump': '06/14/1946','Rowan Atkinson': '01/6/1955'}
# 	print('Welcome to the birthday dictionary. We know the birthdays of:')
# 	for name in birthdays:
# 		print(name)
# 	print('Who\'s birthday do you want to look up?')
# 	name = input()
# 	if name in birthdays:
# 		print('{}\'s birthday is {}.'.format(name, birthdays[name]))
# 	else:
# 		print('Sadly, we don\'t have {}\'s birthday.'.format(name))