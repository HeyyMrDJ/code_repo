# Program for learning tuples (immutable list)

# Creation of tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples don't support changes (immutable) unless you redefine the entire tuple
#dimensions[0] = 250
dimensions = (250, 50)
print("Modified Dimensions")
print(dimensions)

# Single element tuples are supposed to require a trailing comma. I can't seem to make that work unless I drop ths parenthesis. 
my_tuple = 10
my_tuple[0] = 20
print(my_tuple)