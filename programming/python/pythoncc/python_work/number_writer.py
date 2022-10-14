"""Simple program to learn writing to files"""
from encodings import utf_8
import json
import os

numbers = [2, 3, 5, 7, 11, 13]

directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'numbers.json')
with open(filename, 'w', encoding=utf_8) as f:
    json.dump(numbers, f)
