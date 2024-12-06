""" 
    In this program the user is able to continue calculating but cannot start over again or a fresh
"""

from art import logo

print(logo)

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

# Looping through the list of operations
for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:
    selected_symbol = input("Select the operation: ")
    num2 = int(input("Enter the next number: "))

    answer = operations[selected_symbol](num1, num2)

    print(f"{num1} {selected_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
        num1 = answer
    else:
        should_continue = True
 