"""Simple program to learn dumping and loading json data"""
import json
import os

FILE_NAME = 'username.json'

def get_new_username():
    """Prompt for new username"""
    username = input("What is your name? ")
    directory = os.path.dirname(__file__)
    file_name = os.path.join(directory, FILE_NAME)
    with open(file_name, 'w', encoding="utf8") as file:
        json.dump(username, file)
        print(f"We'll remember you when you come back, {username}!")

    return username

def get_stored_username():
    """Get stored username if available"""
    directory = os.path.dirname(__file__)
    file_name = os.path.join(directory, FILE_NAME)
    try:
        with open(file_name, encoding="UTF8") as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

#Load the username, if it has been stored previously
#Otherwise prompt for username to store it
def greet_user():
    """Greet the user by name"""
    username = get_stored_username()

    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
