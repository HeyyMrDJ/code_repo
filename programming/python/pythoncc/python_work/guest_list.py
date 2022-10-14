# Program to add, remove, and interate through a guest list

guest_list = ['Warren Buffet', 'Elon Musk', 'Ron Paul']

for guest in guest_list:
    print(f"\t Hi {guest}, please come to my dinner")

removed_guests = "Elon Musk"
guest_list.remove(removed_guests)
print(f"\nApparently {removed_guests.title()} can't make it. Resending guest list \n")

for guest in guest_list:
    print(f"\t Hi {guest}, please come to my dinner")

print("\nA bigger table was found. Sending new invitations \n")

guest_list.insert(0, 'Charlie Munger')
guest_list.insert(2, 'Paul Tudor Jones')
guest_list.append('Peter Lynch')

for guest in guest_list:
    print(f"\t Hi {guest}, please come to my dinner")

print("\n Apparently I only have room for two people now. Resending guest list \n")

print(len(guest_list))
while len(guest_list) > 2:
    uninvited_guest = guest_list.pop(0)
    print(f"Sorry {uninvited_guest} I don't have enough room now")

invited_guests = guest_list

print(""" 
FINAL GUEST LIST
""")

for guest in invited_guests:
    print(f"\t Hi {guest}, please come to my dinner. These invitations are final")

print(f"\nRemaining names on old guest list: {guest_list}")
print("Removing old names from old list")
while len(guest_list) > 0:
    del guest_list[0]

print(f"Remaining names on old guest list: {guest_list}")