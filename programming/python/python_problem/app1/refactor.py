"Read from text file. Return longest word without repeating characters"
longest_word = ""  # pylint: disable=C0103
# Read file
with open("./words.txt", "r", encoding='UTF8') as f:
    # Pass line into list
    for line in f.readlines():
        # Strip out newlines
        line = line.strip()
        # Pass line into set to strip out repeated characters
        list1 = list(set(line))
        # if len of new list is equal to line. Update longest_word
        if (len(line) == len(list1)) and (len(line) > len(longest_word)):
            longest_word = line

print(f"The longest word without repeated characters: {longest_word}")
