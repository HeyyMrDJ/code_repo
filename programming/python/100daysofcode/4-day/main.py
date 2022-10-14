import random

def tied():
    print("You tied")

def lost():
    print("You lost")

def won():
    print("You won")

def input_validate(player):
    if player not in move_list:
        print("invalid option. You're an idiot")
        quit()

def grade_moves(player, ai):
    if player == "rock" and ai == "rock":
        tied()
    if player == "rock" and ai == "paper":
        lost()
    if player == "rock" and ai == "scissors":
        won()

    if player == "paper" and ai == "rock":
        won()
    if player == "paper" and ai == "paper":
        tied()
    if player == "paper" and ai == "scissors":
        lost()

    if player == "scissors" and ai == "rock":
        lost()
    if player == "scissors" and ai == "paper":
        tied()
    if player == "scissors" and ai == "scissors":
        won()

move_list = ["rock", "paper", "scissors"]

player = input(f"Please choose {move_list}\n").lower()
input_validate(player)

ai = random.choice(move_list)

print(f'Player choice: {player}')
print(f'AI choice: {ai}')

grade_moves(player, ai)