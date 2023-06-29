#Dice Rolling Simulator
import random

do_you = input("Do you want to roll the dice? (y/n) ") # asks if user wants to roll the dice

while do_you == "y": # if user wants to roll the dice, then roll the dice
    print(random.randint(1,6)) # random.randint generates a random integer between 1 and 6
    do_you = input("Do you want to roll the dice? (y/n) ") # asks if user wants to roll the dice again
else: # if user doesn't want to roll the dice, then say goodbye
    print("Goodbye!")