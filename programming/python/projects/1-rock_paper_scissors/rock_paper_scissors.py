"""Project 1 - Rock, Paper, Scissors"""
import random

# Function to check player/computer inputs
def check_input(user_input, computer_input):
    """Function to check input"""
    # Display user and computer decissions
    print(f"\nComputer decission was: {computer_input.title()}")
    print(f"User decission was: {user_input.title()}")

    outcomes = [
        ['Rock', 'Rock', 'tie'],
        ['Rock', 'Paper', 'lose'],
        ['Rock', 'Scissors', 'win'],
        ['Paper', 'Rock', 'lose'],
        ['Paper', 'Paper', 'tie'],
        ['Paper', 'Scissors', 'win'],
        ['Scissors', 'Rock', 'lose'],
        ['Scissors', 'Paper', 'win'],
        ['Scissors', 'Scissors', 'tie'],
    ]
    #Iterate through list to find outcome that matches user and computer choices
    for outcome in outcomes:
        if user_input == outcome[0] and computer_input == outcome[1]:
            return outcome[2]

# Function to display results
def game_over(result):
    """Game Over Function"""
    print("\n")
    if result == 'tie':
        print("\tTied game!")
    if result == 'win':
        print("\tYou Win!")
    if result == 'lose':
        print("\tYou Lose!")
    print("\n")
    exit()

# Function to print welcome screen
def game_intro():
    """Game Intro Function"""
    print("""
    WELCOME TO ROCK, PAPER, SCISSORS!!!

    \tROCK > SCISSORS
    \tPAPER > ROCK
    \tSCISSORS > PAPER
    """)

# Function to get and validate user input
def get_user_input():
    """Function to get user input"""
    # pylint: disable=redefined-outer-name
    user_input = ""
    while user_input not in ['Rock', 'Paper', 'Scissors']:
        user_input = input("Enter Your choice: Rock, Paper, or Scissors\n").title()
    return user_input

# Display welcome screen
game_intro()

# Ask user for input
users_input = get_user_input()

# Randomly generate computer answer
computers_input = random.choice(['Rock', 'Paper', 'Scissors'])

# Compare user input with computer input
GAME_OUTCOME = check_input(users_input, computers_input)

# Display game over depending on result of GAME_OUTCOME
game_over(GAME_OUTCOME)
