""" 
    In this program the user is able to continue calculating and also can start over a fresh.
    
    ~~~~~~~~~~~~This is achieved by recursion method~~
    This is basically calling the function inside itself
    
    NOoTE: There should always be a condition that will make the recursion stop, otherwise it will be an indefinite loop
"""

from art import logo



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

def calculate():
    # print(logo)
    num1 = float(input("Enter the first number: "))

    # Looping through the list of operations
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        selected_symbol = input("Select the operation: ")
        num2 = float(input("Enter the next number: "))

        answer = operations[selected_symbol](num1, num2)

        print(f"{num1} {selected_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start afresh.: ") == 'y':
            num1 = answer
        else:
            should_continue = True
            calculate()
            
calculate()
