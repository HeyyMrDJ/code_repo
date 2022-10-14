# Program for learning ranges and slices

for value in range(6):
    print(value)

numbers = list(range(1, 6, 2))
print(numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares = []
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

new_squares = squares[:]
print(new_squares)
new_squares.append(20)
print(squares)
print(new_squares)

new_squares = squares
print(new_squares)
new_squares.append(20)
print(squares)