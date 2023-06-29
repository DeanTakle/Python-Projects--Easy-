import random # Import the random module

print("Welcome to the Random Number Game!") # Print a welcome message

random_number = random.randint(1, 10) # Generate a random number between 1 and 100
lives = 3 # Set the number of lives to 3
answer_list = [] # Create an empty list for the answers

player_choice = input('Guess an number between 1 and 10') # Get the player's guess
player_choice = int(player_choice) # Convert the player's guess to an integer


if player_choice == random_number:
    print("You win!") # If the player's guess is the same as the random number
elif player_choice == answer_list:
    print("You already guessed that number!") # If the player's guess is the same as a number they already guessed
elif player_choice >=1 or player_choice >=10:
    print("That number is not between 1 and 10!") # If the player's guess is not between 1 and 10
else:
    lives-=1 # Subtract 1 from the number of lives
    answer_list.append(player_choice) # Add the player's guess to the list of answers
    if lives  == 0: # If the player has no lives left
        print("You lose!") # If the player has no lives left
        print("The number was", random_number) # Print the random number
        
print("Thanks for playing!") # Print a goodbye message



