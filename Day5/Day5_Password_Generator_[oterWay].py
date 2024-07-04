#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Randomize the letters
password = []
for letter in range(1, nr_letters+1):
    new_char = random.choice(letters)
    password.append(new_char)

# Deal with numbers
for num in range(1, nr_numbers+1):
    nums = random.choice(numbers)
    password.append(nums)

# Deal with symbols
for symbol in range(1, nr_symbols+1):
    extracted_symbol = random.choice(symbols)
    password.append(extracted_symbol)
    

print(password)
random.shuffle(password)
print(password)

# Change the array items into a string by looping through and concatenate all the characters
new_password = ""
for pass_char in password:
    new_password += pass_char
    
print(new_password)             


## ///////////////************** DOCUMENTATION**************//////////////////////


## Create the password array that will be accepting all the characters sent into it

## Then loop through each array (letters, symbols and numbers)

## range is between 1 and the number of times/characters a user wants in their password obtained by adding a 1 to the number BECAUSE range(1, 3) will make 3 exclusive so to include it we use 4, so in the number got from user we add 1

## later, the characters in the password array, can be changed into a string by looping through and concatenate the characters in the new string that can be created to keep all the characters extracted from the password array

## shuffling will help to make sure that the characters are not in a particular order, say letters first, followed by numbers and followed by symbols but rather a mixture.

## NOTE************** Its better not to put the shuffle() function in the variable, but rather just perform the shuffling on a new line and then re-print whatever you have been shuffling         
    ## same applies to the .append() function