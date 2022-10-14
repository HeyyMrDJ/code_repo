"Interview problem"

FILE_NAME = "words.txt"


def check_longest(long_list: list) -> str:
    "Function to check longest word from list and return longest word"
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


def format_lines(line_format: str) -> str:
    "Function to format lines for consistency"
    line_format = line_format.strip()
    line_format = line_format.lower()

    return line_format


def check_contents(contents_check, contents_list):
    "Function to open file"
    for line in contents_check:
        line = format_lines(line)
        new_list = [line]
        test = check_repeating(new_list)
        if test == "NONE":
            contents_list.append(line)

    return check_longest(contents_list)


def main(file_name):
    "Main Function"
    with open(file_name, "r", encoding='UTF8') as file:
        contents = file.readlines()
        list1 = []
        print(f"The longest word is: {check_contents(contents, list1)}")

    return check_contents(contents, list1)


if __name__ == "__main__":
    main(FILE_NAME)
