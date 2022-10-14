"""Write Message"""
import os
my_dir = os.path.dirname(__file__)
filename = os.path.join(my_dir, 'programming.txt')
with open(filename, 'a', encoding="UTF8") as file_object:
    file_object.write("I LOVE PROGRAMMING \n")
    file_object.write("I like creating games too \n")
