# Program to learn functions

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name[0]} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
formatted_musician = get_formatted_name(musician['first'], musician['last'])
print(formatted_musician)

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")

    first_name = input("First name: ")
    if first_name == 'q':
        break

    last_name = input("Last name: ")
    if last_name == 'q':
        break
    
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\n\tHello, {formatted_name}")
