# Program to sort through a list of cars

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))

print("\nHere is the sorted list backwards")
print(sorted(cars, reverse=True))

print("\nHere is the list backwards")
cars.reverse()
print(cars)
# Reverse again to put list back in original order (reverse is permanent, reverse againto undo)
cars.reverse()

print("\nHere is the original list again")
print(cars)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())