import random

# 3 options to chose from ('Rock', 'Paper', 'Scissors')
choices = ['Rock', 'Paper', 'Scissors']

# Player and computer scores
player_score = 0
computer_score = 0

#Getting Players choice
def player_choice():
    global choices # Global variable
    player = input("Rock, Paper, or Scissors? ").capitalize() # Capitalize the first letter of the input
    if player in choices: # If the player's choice is in the list of choices
        return player # Return the player's choice
    else:
        print("Invalid choice, try again.") # If the player's choice is not in the list of choices
        return player_choice() # Run the function again
    
#Getting Computers choice
def computer_choice():
    return random.choice(choices) # Return a random choice from the list of choices

def game():
    global player_score, computer_score
    pChoice = player_choice() # Get the player's choice
    cChoice = computer_choice() # Get the computer's choice
    print("You chose", pChoice) # Print the player's choice
    print("Computer chose", cChoice) # Print the computer's choice
    if pChoice == cChoice:
        print("It's a tie!") # If the player's choice is the same as the computer's choice
    elif pChoice == 'Rock' and cChoice == 'Scissors':
        print("You win!") # If the player's choice is Rock and the computer's choice is Scissors
        player_score += 1 # Add 1 to the player's score
    elif pChoice == 'Paper' and cChoice == 'Rock':
        print("You win!") # If the player's choice is Paper and the computer's choice is Rock
        player_choice += 1
    elif pChoice == 'Scissors' and cChoice == 'Paper':
        print("You win!") # If the player's choice is Scissors and the computer's choice is Paper
        player_score += 1
    else: 
        print("You lose!")
        computer_score += 1

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("First to 3 wins!")
    while player_score < 3 and computer_score < 3:
        game()
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
    if player_score == 3:
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (Y/N) ").capitalize()
    if again == 'Y':
        main()
    else:
        print("Thanks for playing!")
