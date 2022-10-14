"Python problem"
import os


def check_longest(long_list):
    "test"
    longest_word = ""
    for my_line in long_list:
        if len(my_line) > len(longest_word):
            longest_word = my_line
    return longest_word


def check_repeating(repeating_list: list) -> str:
    "Function to check for repeating characters"

    for line in repeating_list:
        new_list = []
        for char in line:
            if char in new_list:
                return "FOUND"
            new_list.append(char)

    return "NONE"


directory = os.path.dirname(__file__)
my_filename = os.path.join(directory, "words.txt")
list1 = []
longest_word = ""

with open(my_filename, encoding="UTF8") as file:
    contents = file.readlines()

for line in contents:
    list1.append(line.strip())

# for my_line in list1:
#    print(len(my_line))


for my_line in list1:
    if len(my_line) > len(longest_word):
        repeat_list = [my_line]
        new_str = check_repeating(repeat_list)
        if new_str == "NONE":
            longest_word = my_line

    # if len(list1[my_line]) > len(longest_word):
    #    longest_word = my_line
    # print(type())
# print(contents)
# print(list1)

print(longest_word)
