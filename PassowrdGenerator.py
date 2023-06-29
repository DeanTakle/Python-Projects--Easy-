#Password Generator
import random 
import string

uppperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # string.ascii_uppercase
lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz" # string.ascii_lowercase
numbers = "0123456789" # string.digits
symbols = "[]{}()*;/,._-" # string.punctuation

howlong = int(input("How long do you want your password to be? ")) # asks for password length
password = "".join(random.sample(uppperCaseLetters + lowerCaseLetters + numbers + symbols, howlong))# generates password, random.sample randomly selects characters from the string, "".join joins the characters together
print(password)
