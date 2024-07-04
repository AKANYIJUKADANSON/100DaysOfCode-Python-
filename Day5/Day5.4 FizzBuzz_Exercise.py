# ********************* FizzBuzz Game Exercise *************
# Your program should print each number from 1 to 100 in turn
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# If the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"






for num in range(1, 101):
    if num % 3 == 0:
        num = "Fizz"
    elif num % 5 == 0:
        num = "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    print(num)
    
# The code above will not cater for the FizzBuzz option because
    # In the if .. elif.. statement, the first option to be true will be executed, so that means the number divisible by both 3 and 5 wll not be worked on since the sttmt has already obtained the true value/option

# ~~~~~~~~~~~~~~SOLUTION~~~~~~~~~~~
    # The solution is to re-structure the code/ if..elif.. statements, so that we first test the number that is divisible by both 3 and 5 for FizzBuzz, then go ahead to test for those divisible by 3 for fizz and those divisible by 5 for Buzz
    
    
    
# 1 to 100 numbers
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)