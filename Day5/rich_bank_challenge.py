import random

# First enter the names of people that will be part of the game
names = input("Enter names separated by a comm and space: ")

# Generate the list/array of the names provided using the split function
nameList = names.split(", ")   
# Get the total no. of items in the list
# To take care of the indicies, we have to subtract 1 from the totalNumOfItems in the list so that we dont always get the "out of range" coz if totalItemCount = 6, then index will be 0, 1, 2, 3, 4, 5 only with 6 excluded
numOfItems = len(nameList)-1
# Get a random value using a range of 0 and total num of items
randomPersonIndex = random.randint(0, numOfItems)
print(f"Name list: {nameList}")
print(f"Index is: {randomPersonIndex}")
billPayer = nameList[randomPersonIndex]

print(f"{billPayer} is paying today :)")

# This can also be achieved easily by using the  random.choice() function