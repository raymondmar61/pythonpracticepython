#Practice Python 016 Password Generator
#Write a password generator in Python. Be creative with how you generate passwords strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your runtime code in a main method.  Add exercise description 051717.

import random
passwordcharacters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","I","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","`","~",",",".","/",";","‘","[","]","<",">","?",":","\""",","{","}","|","_","-","+","=","\\"] #92 items in passwordcharacters list
userpassword = []
numberofcharacters = input("How many characters in your password? ")
numberofcharacters = int(numberofcharacters)
counter = 1 #counter starts at 1 because number of characters user enters count starts at 1
while counter <= numberofcharacters:
	userpassword.append(passwordcharacters[random.randint(0,len(passwordcharacters)-1)]) #endnding number is minus 1 because list count begins at 0.  92 items in passwordcharacters list.  Count starts at 0.
	counter += 1
print(userpassword)
userpasswordjoin = "".join(userpassword)
print(userpasswordjoin)