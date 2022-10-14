"""Simple program to learn file reading"""
import os
directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'pi_digits.txt')


try:
    with open(filename, encoding="UTF8") as file_object:
        lines = file_object.readlines()
    # pylint: disable=invalid-name
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    print(len(pi_string))
except FileNotFoundError:
    print(f"ERROR: {filename} does not exist")
