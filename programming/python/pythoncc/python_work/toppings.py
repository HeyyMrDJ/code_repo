"""Program to use multiple lists with conditionals"""

available_toppings = [
    'mushrooms',
    'pineapple',
    'olives',
    'green pepper',
    'pepperoni',
    'extra cheese'
    ]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!\n")

# Using a list inside a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
