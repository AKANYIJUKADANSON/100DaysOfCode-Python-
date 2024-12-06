def total(firstNumber, secondNumber):
    if firstNumber == 0 and secondNumber == 0:
        return "Please enter the numbers!"
    
    return firstNumber + secondNumber


print(total(int(input("Enter the first number: \n")), int(input("Enter the second number: \n"))))

