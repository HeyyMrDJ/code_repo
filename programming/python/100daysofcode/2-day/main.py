print("Welcome to the tip calculator!")

bill = float(input("What was the bill amount? "))

percent = float("0."+input("What percentage would you like to tip? "))

tip = round(bill * percent, 2)

print("Tip amount: $"+ str(tip))

print("Total amount is: $"+ str(tip+bill))