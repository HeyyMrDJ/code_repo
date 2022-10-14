"""Number Reader"""
import json
import os

my_dir = os.path.dirname(__file__)
filename = os.path.join(my_dir, 'numbers.json')
with open(filename, encoding="UTF8") as f:
    numbers = json.load(f)

print(numbers)
