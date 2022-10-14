"""Simple program to learn opening files and spliting"""
import os
directory = os.path.dirname(__file__)
my_filename = os.path.join(directory, 'alice.txt')

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding="UTF8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"ERROR: {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")
        #print(words)

count_words(my_filename)
