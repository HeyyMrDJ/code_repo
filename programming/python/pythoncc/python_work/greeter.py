# Program to learn functions

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}")

greet_user('jesse')
print(greet_user.__doc__)