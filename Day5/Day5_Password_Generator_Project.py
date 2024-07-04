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
lettersPassword = ""
for letter in range(1, nr_letters+1):
    lettersPassword = lettersPassword + letters[letter]
# print(lettersPassword)

# Deal with numbers
numberPassword = ""
for num in range(1, nr_numbers+1):
    numberPassword = numberPassword + numbers[num]
# print(numberPassword)

# Deal with symbols
symbolsPassword = ""
for symbol in range(1, nr_symbols+1):
    symbolsPassword = symbolsPassword + symbols[symbol]
# print(symbolsPassword)

# Combined password
password = lettersPassword + numberPassword + symbolsPassword

shuffledPassword = ''.join(random.sample(password, len(password)))
print(password)
print(shuffledPassword)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P