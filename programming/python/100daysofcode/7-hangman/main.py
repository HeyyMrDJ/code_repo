import random
from hangman_words import word_list
#=====================================================================================================================================================================
# global variables and lists


player_lives = 6 # Head, torso, right leg, left leg, right arm, left arm

word_selected = []
word = []
player_board = []

#=====================================================================================================================================================================
# Functions

def game_setup():
    global word_selected
    global word
    global player_board
    word_selected = random.choice(word_list)

    # Create lists for word and player boards
    word = []
    player_board = []
    #Populate lists for word and player board
    for char in word_selected:
        word.append(char)
        player_board.append('_')

    print(f"DEBUG {word}")

def game_won():
    print("\n\n")
    print("""
    =====================================================================
                                YOU WON!!!
                            
    =====================================================================
    """)
    print(f"\n The word was: {word_selected}\n\n")
    quit()

def game_over():
    print("\n\n")
    print("""
    =====================================================================
                            YOU LOST!
                            GAME OVER
    =====================================================================
    """)
    print(f"\n The word was: {word_selected}\n\n")
    quit()

def print_hud():
    print("\n\n")
    print(player_board)
    print(f"Player lives: {player_lives}")

def game_loop():
    if player_lives == 0:
        game_over()
    if player_board == word:
        game_won()
    print_hud()
    player_guess()

def player_guess():
    global player_lives

    guess = input("Please enter a letter\n").lower()
    if len(guess) > 1:
        print("\nPlease enter a single character\n")
        player_guess()

    counter = 0

    if guess in word:
        for char in word:
            if guess == char:
                player_board[counter] = guess
            counter += 1
    else:
        player_lives -= 1

#=====================================================================================================================================================================
# Active code

game_setup()
while True:
    game_loop()