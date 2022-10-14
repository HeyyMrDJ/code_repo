import sys

heading = """
==============================================================================================
                                    TREASURE ISLAND
==============================================================================================

WELCOME TO TREASURE ISLAND
YOUR MISSION (if you choose to accept it) IS TO FIND THE TREASURE
"""

def game_over():
    print("Sorry you failed this challenge. Please try again")
    quit()

print(heading)

if input("Left or Right?\n").lower() == "right":
    game_over()
if input("Swim or Wait?\n").lower() == "swim":
    game_over()
if input("Red, Blue, or Yellow door?\n").lower() == ("blue" or "red"):
    game_over()

print("\n\n\nCongrats! You have found the treasure")

