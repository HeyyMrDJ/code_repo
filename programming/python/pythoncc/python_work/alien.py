# Program for learning dictionaries

#Create dictionary and print values
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

# Change value
alien_0['color'] = 'red'
print(alien_0['color'])

# Delete key
alien_0['temp'] = 'test'
print(alien_0)
del alien_0['temp']
print(alien_0)

# get can be used to search key value pairs and return a message if pair does not exist. If no second argument is passed 'None' is returned
get_color = alien_0.get('color', "color is not defined")
print(get_color)

# Create new dictionary 
alien_1 = {'color': 'purple', 'points': 10}

# Create dictionary and nest the previous dictionaries
aliens = [alien_0, alien_1]
for alien in aliens:
    print(alien)

# Remove dictionary and create new aliens list
alien_list = []

# Create 30 alien dictionaries
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_list.append(new_alien)

print("\n")

for alien in alien_list[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in alien_list[:5]:
    print(alien)

print(f"Total number of aliens: {len(alien_list)}")

