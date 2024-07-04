import random

stringi = ['e', 'f', 'g', 'h', 'i']
new_array = []
# new_array.append('hello')
for char in range(1, 3):
    # Here we get a character from the list using the random.choice() functions
    new_char = random.choice(stringi)
    # Append/insert every character extracted into the array
    new_array.append(new_char)

# ltr = random.choice(stringi);
print(new_array)