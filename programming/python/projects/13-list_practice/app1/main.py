"list practice"


list1 = ["dank", "memes", "melt", "steel", "beems", "yes", "yes", "no", "no"]
list2 = ["dank", "melt", "yes", "yes", "no", "no"]


def check_duplicate(parse_list: list) -> str:
    "Function to check for duplicates"
    for item in parse_list:
        parse_list.remove(item)

        if item in parse_list:
            dup_item = item
            return dup_item

    return "No duplictate"


def list_reverse(reverse_list: list) -> list:
    "Function to reverse list"
    return reverse_list[::-1]


def check_repeating(repeating_list: list) -> str:
    "Function to check for repeating characters"

    for line in repeating_list:
        new_list = []
        for char in line:
            if char in new_list:
                print(line)
                return f"{char} is repeating"
            new_list.append(char)

    return "No repeating characters found"


# TEST_ITEM = check_duplicate(list1)
# print(TEST_ITEM)
#
# TEST_ITEM = check_duplicate(list_reverse(list1))
# print(TEST_ITEM)

char_item = check_repeating(list1)
print(char_item)
