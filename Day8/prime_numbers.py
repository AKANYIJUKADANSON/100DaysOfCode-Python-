
def checkPrimeNumber(num):
    is_prime = True
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

number = int(input("Enter number to check: "))
checkPrimeNumber(number)