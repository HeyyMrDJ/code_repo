# Project 2 Tic-tac-toe

# Display welcome screen


# BOARD
#          1    2    3
#    A  ____|____|____ 
#    B  ____|____|____ 
#    C      |    |     
#
# RULES
# If A1, A2, A3 = 3 user won, if -3 computer won
# If B1, B2, B3 = 3 user won, if -3 computer won
# If C1, C2, C3 = 3 user won, if -3 computer won
# If A1, B1, C1 = 3 user won, if -3 computer won
# If A2, B2, C2 = 3 user won, if -3 computer won
# If A3, B3, C3 = 3 user won, if -3 computer won
# if A1, B2, C3 = 3 user won, if -3 computer won
# if A3, B2, C1 = 3 user won, if -3 computer won
# If can't continue = user and computer tie

# Create lists to match board. Blank item added to first item to allow board and list item numbers to match (A1 = list_a[1] instead of list_a[0])
list_a = [0, 0, 0, 0]
list_b = [0, 0, 0, 0]
list_c = [0, 0, 0, 0]
list_y = [0, 0, 0, 0, 0]
list_x = [0, 0, 0]
move_character = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Function to update lists
def update_lists():
    list_y[0] = list_a[1] + list_b[2] + list_c[3]
    list_y[1] = list_a[1] + list_b[1] + list_c[1]
    list_y[2] = list_a[2] + list_b[2] + list_c[2]
    list_y[3] = list_a[3] + list_b[3] + list_c[3]
    list_y[4] = list_a[3] + list_b[2] + list_c[1]

    list_x[0] = list_a[1] + list_a[2] + list_a[3]
    list_x[1] = list_b[1] + list_b[2] + list_b[3]
    list_x[2] = list_c[1] + list_c[2] + list_c[3]

    if list_a[1] == 1:
        move_character[0] = 'X'
    if list_a[1] == -1:
        move_character[0] = 'O'
    if list_a[2] == 1:
        move_character[1] = 'X'
    if list_a[2] == -1:
        move_character[1] = 'O'
    if list_a[3] == 1:
        move_character[2] = 'X'
    if list_a[3] == -1:
        move_character[2] = 'O'

    if list_b[1] == 1:
        move_character[3] = 'X'
    if list_b[1] == -1:
        move_character[3] = 'O'
    if list_b[2] == 1:
        move_character[4] = 'X'
    if list_b[2] == -1:
        move_character[4] = 'O'
    if list_b[3] == 1:
        move_character[5] = 'X'
    if list_b[3] == -1:
        move_character[5] = 'O'

    if list_c[1] == 1:
        move_character[6] = 'X'
    if list_c[1] == -1:
        move_character[6] = 'O'
    if list_c[2] == 1:
        move_character[7] = 'X'
    if list_c[2] == -1:
        move_character[7] = 'O'
    if list_c[3] == 1:
        move_character[8] = 'X'
    if list_c[3] == -1:
        move_character[8] = 'O'

def check_board():
    if 3 in list_y:
        game_over('win')
    if -3 in list_y:
        game_over('lose')
    if 3 in list_x:
        game_over('win')
    if -3 in list_x:
        game_over('lose')

def get_user_input():
    if 0 not in list_a[1:] and 0 not in list_b[1:] and 0 not in list_c[1:]:
        game_over('tie')
    user_input = input("Enter row[column] to make your move (eg. A1): ")

    if user_input[0].title() not in ['A', 'B', 'C']:
        print(f"{user_input[0].title()} is not a valid row")
        get_user_input()
    if (user_input[1]) not in ['1', '2', '3']:
        print(f"{user_input} is not a valid column")
        get_user_input()
    if int(user_input[1]) not in [1, 2, 3]:
        print(f"{user_input[1]} is not a valid column")
        get_user_input()
    if user_input[0].title()in ['A', 'B', 'C'] and int(user_input[1]) in [1, 2, 3]:
        row = str(user_input[0]).title()
        column = int(user_input[1])
        make_move(row, column, 'User')

def make_move(row, column, player):
    if row == 'A' and column == 1 and player == 'User':
        if list_a[1] == 0:
            list_a[1] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'A' and column == 1 and player == 'Computer':
        list_a[1] = -1
    if row == 'B' and column == 1 and player == 'User':
        if list_b[1] == 0:
            list_b[1] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'B' and column == 1 and player == 'Computer':
        list_b[1] = -1
    if row == 'C' and column == 1 and player == 'User':
        if list_c[1] == 0:
            list_c[1] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'C' and column == 1 and player == 'Computer':
        list_c[1] = -1
    if row == 'A' and column == 2 and player == 'User':
        if list_a[2] == 0:
            list_a[2] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'A' and column == 2 and player == 'Computer':
        list_a[2] = -1
    if row == 'B' and column == 2 and player == 'User':
        if list_b[2] == 0:
            list_b[2] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'B' and column == 2 and player == 'Computer':
        list_b[2] = -1
    if row == 'C' and column == 2 and player == 'User':
        if list_c[2] == 0:
            list_c[2] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'C' and column == 2 and player == 'Computer':
        list_c[2] = -1
    if row == 'A' and column == 3 and player == 'User':
        if list_a[3] == 0:
            list_a[3] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'A' and column == 3 and player == 'Computer':
        list_a[3] = -1
    if row == 'B' and column == 3 and player == 'User':
        if list_b[3] == 0:
            list_b[3] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'B' and column == 3 and player == 'Computer':
        list_b[3] = -1
    if row == 'C' and column == 3 and player == 'User':
        if list_c[3] == 0:
            list_c[3] = 1
        else: 
            print("Not Empty! Please try again.")
            get_user_input()
    if row == 'C' and column == 3 and player == 'Computer':
        list_c[3] = -1
    update_lists()
    check_board()
    display_board()

def computer_move():
    if list_a[1] == 0:
        make_move('A', 1, 'Computer')
        return
    if list_a[2] == 0:
        make_move('A', 2, 'Computer')
        return
    if list_a[3] == 0:
        make_move('A', 3, 'Computer')
        return
    if list_b[1] == 0:
        make_move('B', 1, 'Computer')
        return
    if list_b[2] == 0:
        make_move('B', 2, 'Computer')
        return
    if list_b[3] == 0:
        make_move('B', 3, 'Computer')
        return
    if list_c[1] == 0:
        make_move('C', 1, 'Computer')
        return
    if list_c[2] == 0:
        make_move('C', 2, 'Computer')
        return
    if list_c[3] == 0:
        make_move('C', 3, 'Computer')
        return

def game_loop():
    while True:
        get_user_input()
        computer_move()

def display_board():

    print(f"""
                 TicTacToe\n                    
                {move_character[0]} |  {move_character[1]}  |  {move_character[2]}
              ---------------
                {move_character[3]} |  {move_character[4]}  |  {move_character[5]}
              ---------------
                {move_character[6]} |  {move_character[7]}  |  {move_character[8]}
      
    """)

def game_over(result):
    display_board()
    if result == 'win':
        print("""
                YOU WIN!!!
        """)
    if result == 'lose':
        print("""
                YOU LOSE!!!
        """)
    if result == 'tie':
        print("""
                NO WINNER!!!
        """)
    quit()

game_loop()

# Get user input

# Check if game over

# Get computer input

# Check if game over

# Display game over