import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
specials = ["#", "@", "!", "(", ")"]

min_letters = int(input("How many letters?\n"))
min_specs = int(input("How many special characters?\n"))
min_numbers = int(input("How many numbers?\n"))

selected_chars = random.choices(specials, k=min_specs) + random.choices(letters, k=min_letters) + random.choices(numbers, k=min_numbers)

random.shuffle(selected_chars)
password = ""
for chars in selected_chars:
    password += chars

print(password)