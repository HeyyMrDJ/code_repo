'Mod'
import os
directory = os.path.dirname(__file__)
my_filename = os.path.join(directory, './test.txt')

file1 = open(my_filename, "r", encoding="UTF8")

for line in file1:
    print(line)
