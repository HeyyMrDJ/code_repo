# Program to use conditionals with strings

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user == 'bob':
    print(f"{user.title()}, we told you not to come back here")
elif user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()}, you are banned!")

