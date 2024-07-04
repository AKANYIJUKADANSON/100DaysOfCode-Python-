# Get user's pizza size
pizza_size = input("What pizza size would you like to order? S = Small, M = Medium, L = Large:  ")

bill = 0
if pizza_size == "S":
    size = "S"
    bill = 15
    print("Your bill is $15")
elif pizza_size == "M":
    size = "M"
    bill = 20
    print("Your bill is $20")
else:
    size = "L"
    bill = 25
    print("Your bill is $25")
    
# Ask for pepperoni addition
add_pepperoni = input("Would you like to add pepperoni? Y = Yes, N = No:  ")
if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
        print(f"Your bill is ${bill}")
    else:
        bill = bill + 3
        print(f"Your bill is ${bill}")

# Ask for addition of cheese
extra_cheese = input("Would you like to add extra cheese? Y = Yes, N = No:  ")
if extra_cheese == "Y":
    bill = bill + 1
    print(f"Your bill is ${bill}")
else:
    print(f"Your bill is ${bill}")
        