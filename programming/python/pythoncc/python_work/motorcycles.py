# Program about a list of motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(0, 'honda')
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
del motorcycles[0]
print(motorcycles[0])

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles.remove('ducati')
print(motorcycles)