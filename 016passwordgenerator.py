from random import * #instead of import random for which I must type random. in the random function
# number = randint(0,10)
# print(number)

#Do not use the random.sample() function because you will get weaker passwords.  Sample does not reuse characters.
# items = ["1", "2", "3", "4", "a", "b","c","d"]
# passwordlength = int(input("Enter passwordlength: "))
# password = sample(items,passwordlength)
# password = "".join(password)
# print(password)

itemsall = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","I","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","`","~",",",".","/",";","‘","[","]","<",">","?",":","\""",","{","}","|","_","-","+","=","\\"]
print(len(itemsall)) #92
passwordlength = int(input("Enter password length: "))
newpassword = []
for eachpasswordcharacter in range(0,passwordlength):
	newpassword.append(itemsall[randint(0,91)]) #(itemsall(randint(1,92))) is incorrect, need brackets.  Remember print(itemsall[60]) to get something from a list
print(newpassword)
newpassword = "".join(newpassword)
print(newpassword)

# lowercase = "abcdefghijklmnopqrstuvwxyz"
# uppercase = lowercase.upper()
# numbers = "0123456789"
# symbols = "~`!@#$%^&*(),./;'[]\<>?:\"{}|"
# lowercase = list(lowercase)
# uppercase = list(uppercase)
# numbers = list(numbers)
# symbols = list(symbols)
# print(lowercase)
# print(uppercase)
# print(numbers)
# print(symbols)
# # print(password)
# def jointlists(lowercase, uppercase, numbers, symbols):
# 	print(lowercase + uppercase + numbers + symbols)
# 	return(lowercase + uppercase + numbers + symbols)
# password = (jointlists(lowercase, uppercase, numbers, symbols))
# print(len(password))
# passwordlength = int(input("Enter password length: "))
# newpassword = []
# for eachpasswordcharacter in range(0,passwordlength):
# 	newpassword.append(password[randint(0,89)]) #(itemsall(randint(0,89))) is incorrect, need brackets.  Remember print(itemsall[60]) to get something from a list
# newpassword = "".join(newpassword)
# print(newpassword)