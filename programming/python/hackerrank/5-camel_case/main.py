'Challenge problem camelCase 4'

import sys


def string_parser(string_parser_string: str) -> tuple and str:
    'Function to parse strings'
    string_parser_tuple = (string_parser_string[0], string_parser_string[2])
    string_parser_string = string_parser_string.strip(string_parser_string[0])
    string_parser_string = string_parser_string[3:]
    return string_parser_tuple, string_parser_string


def string_splitter(string_splitter_string: str) -> str:
    'Function to split strings'
    split_list = []
    my_new_string = ''
    for i, char in enumerate(string_splitter_string):
        if char.isupper() and i == 0:
            split_list.append(char)
        elif char.isupper():
            split_list.append(' ')
            split_list.append(char)
        else:
            split_list.append(char)
    return my_new_string.join(split_list)


def string_combiner(string_combiner_string: str) -> str:
    'Function to combine strings'
    return string_combiner_string.replace(' ', '')


def string_manipulator(
        string_manipulator_string: str,
        string_manipulator_my_tuple: tuple) -> str:
    'Function to manipulate based on Class, Method, or Variable specification'
    if string_manipulator_my_tuple[1] == 'M':
        if string_manipulator_string[-2:] == '()':
            string_manipulator_string = string_manipulator_string.strip('()')
            return string_splitter(string_manipulator_string).lower()
        else:
            string_manipulator_string += '()'
            return string_combiner(camel_case(string_manipulator_string))

    if string_manipulator_my_tuple[1] == 'V':
        if ' ' in string_manipulator_string:
            return string_combiner(camel_case(string_manipulator_string))

        return string_splitter(string_manipulator_string).lower()
    if string_manipulator_my_tuple[1] == 'C':
        if ' ' in string_manipulator_string:
            return string_combiner(string_manipulator_string.title())
        if string_manipulator_string.lower() == string_manipulator_string:
            return string_manipulator_string.title()

        return string_splitter(string_manipulator_string).lower()


def camel_case(camel_case_string: str) -> str:
    'Function to convert strings to camel case'
    camel_case_string = camel_case_string.title()
    return camel_case_string[0].lower() + camel_case_string[1:]


new_list = []
lines = sys.stdin.readlines()
for line in lines:
    new_list.append(line.strip('\r\n'))
for string in new_list:
    my_tuple, my_string = string_parser(string)
    print(string_manipulator(my_string, my_tuple))
