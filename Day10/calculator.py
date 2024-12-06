from art import logo

# print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2
# Division
def divide(n1, n2):
    return n1 / n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2


operations = {
    "+":add, 
    "-":subtract, 
    "/":divide, 
    "*":multiply
}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Looping through the list of operations
for symbol in operations:
    print(symbol)

# Ask the use for which operation they want to do using the sysmbols
selected_symbol = input("Select the operation to do from the list above: ")

answer = operations[selected_symbol](num1, num2)
# Make the calculations
print(f"{num1} {selected_symbol} {num2} = {answer}")
