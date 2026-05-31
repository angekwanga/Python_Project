print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12 or 15? "))
totalBill = bill + bill * tip / 100
people = int(input("How many people to split the bill? "))
print("Each person should pay:" + str(round(totalBill / people, 2)))