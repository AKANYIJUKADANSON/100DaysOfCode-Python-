print("Welcome to the tip calculator.")
# Prompt user to enter the total bill
total_bill = float(input("What was the total bill?  $"))
# Prompt user to enter the percentage tip
tip = int(input("What percentage tip would you like togive? 10, 12, 0r 15:   "))
percentage_tip = tip / 100
tip_amount = percentage_tip * total_bill

# Remaining amount after tip addition
total_bill_with_tip = total_bill + tip_amount

# Prompt user to enter the number of people to split the bill
people = int(input("How many people to split the bill? "))

individual_bill = round((total_bill_with_tip / people), 2)
# Each person's pay
print(f"Each person should pay: {individual_bill}")