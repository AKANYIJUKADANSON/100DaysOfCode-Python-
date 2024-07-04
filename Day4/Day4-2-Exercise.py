import random
print("Welcome to WHO DE BUY Game!")
names = input("Enter all the names separate by a comma and space\n")

# Change the string characters to a list using the split fn
name_list = names.split(", ")

# get length of the list
list_length = len(name_list)
# print(f"Number of items: {list_length}")
# Get random name using index
buyer = name_list[random.randint(0, list_length-1)]

# print the random name from the list
print(f"{buyer} is buying the drink today")