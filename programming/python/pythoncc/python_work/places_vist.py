# Program to sort through a list of places I'd like to visit

places = ['Tennessee', 'Kentucky', 'Texas', 'Florida', 'Arizona']

print("Here is a list of places I'd like to visit: ")
print(places)

print("Here is a sorted list of places I'd like to visit: ")
print(sorted(places))

print("Here is the original list again: ")
print(places)

print("Here is a reversed list of places I'd like to visit: ")
places.reverse()
print(places)

# Reverse again to put list back in original order (reverse is permanent, reverse againto undo)
print("Here is the original list again: ")
places.reverse()
print(places)

print("Here is a sorted list: ")
places.sort()
print(places)

print("Here is a list of places sorted in reverse: ")
places.sort(reverse=True)
print(places)
