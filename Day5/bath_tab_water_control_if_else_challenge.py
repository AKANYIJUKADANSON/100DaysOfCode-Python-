# bathTabHeight = 800
# water_level = int(input("Enter water level: "))
# if water_level > bathTabHeight:
#     print("Status: Start Draining bath tab")
# else:
#     print("Status: Keep filling bath tab")
    
    
# GRADING SYSTEM
    
# mark = int(input("Enter mark to determine your grade: "))
# if mark >= 90:
#     print("Grade: A")
# elif mark >= 80:
#     print("Grade: B")
# elif mark >= 70:
#     print("Grade: C")
# elif mark >= 60:
#     print("Grade: D")
# elif mark >= 50:
#     print("Grade: E")
# elif mark >= 40:
#     print("Grade: F")
# else:
#     print("Grade: UNGRADED")


# PIZZA ORDER SYSTEM

# Capture pizza size from user
pizza_size = input("Which pizza size do you want to order? S - Small, L - Large, M - Medium:  ").upper()

# Capture status for pepperoni from user
pepperoni = input("Do you want pepperoni added? Y - Yes, N - No: ").upper()
 
# Capture extra cheese from user
extraCheese = input("Do you want cheese added? Y - Yes, N - No: ").upper()

# Initialize the price to 0
price = 0
if pizza_size == "S" or pizza_size == "s":
    price = 15
    
    if pepperoni == "Y":
        price = price + 2
    
    if extraCheese == "Y":
        price = price + 1;
        
elif pizza_size == "M" or pizza_size == "m":
    price = 20
    
    if pepperoni == "Y":
        price = price + 3
    
    if extraCheese == "Y":
        price = price + 1;
else:
    price = 25
    
    if pepperoni == "Y":
        price = price + 3
        
    if extraCheese == "Y":
        price = price + 1;
           
# print("Piza Size: " + pizza_size)
# print("Pepperoni: " + pepperoni)

# Output bill
print("Your final bill is: ", price)