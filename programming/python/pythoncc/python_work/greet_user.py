"""Simple program to learn how to load JSON data from file"""
import json
import os

directory = os.path.dirname(__file__)
FILENAME = os.path.join(directory, 'username.json')

with open(FILENAME, encoding="UTF8") as file:
    username = json.load(file)
    print(f"Welcome back, {username}!")
