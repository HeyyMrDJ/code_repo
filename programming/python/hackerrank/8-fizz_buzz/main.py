'Sample test'

# If number divisible by 3 replace with Fizz

# If number divisable by 5 replace with Buzz

# If number divisable by 3 and 5 replace with FizzBuzz
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def fizz_buzz(fizz_list: list) -> list:
    'Function to FizzBuzz'
    return_list = []
    for numb in fizz_list:
        if numb % 3 == 0 and numb % 5 == 0:
            return_list.append("FizzBuzz")
        elif numb % 5 == 0:
            return_list.append("Buzz")
        elif numb % 3 == 0:
            return_list.append("Fizz")
        else:
            return_list.append(numb)
    return return_list


list1 = 15
print(fizz_buzz(list1))

def fizz_buzz(fizz_list: int) -> list:
    'Function to FizzBuzz'
    return_list = []
    for numb in range (1, fizz_list):
        if numb % 3 == 0 and numb % 5 == 0:
            return "FizzBuzz"
        elif numb % 5 == 0:
            return "Buzz"
        elif numb % 3 == 0:
            return "Fizz"
        else:
            return numb