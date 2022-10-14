name = "Bob"
message = f"Hi {name}, would you like to learn some Python today?"
print(message)

print(f"Lowercase: {name.lower()}")
print(f"Uppercase: {name.upper()}")
print(f"Titlecase: {name.title()}")


author = "Albert Einstein"
message = "Everything should be made as simple as possible, but not simpler"
print(message + " ~" + author)


whitespace_name = "\n Bob"
print(whitespace_name)
print(whitespace_name.rstrip().lstrip())
print(whitespace_name.strip())