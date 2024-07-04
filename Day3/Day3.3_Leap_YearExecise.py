print("Welcome to leap year checker!")
year = int(input('Enter the year to check: '))

# Yr should be evenly didvisibly by 4
    # Yr shouldn't also be evenly divisible by 100
        # unless the yr is also evenly divisible by 400


# Yr should be evenly didvisibly by 4
# if year % 4 == 0:
#     if year % 100 != 0:
#         print(f"{year} is not a leap year (not evenly didvisibly by 100)")
#     else:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year (not evenly didvisibly by 400)")
    
# else:
#     print(f"{year} is not a leap year (not evenly didvisibly by 4)")


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year (not evenly didvisibly by 400)")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year (not evenly didvisibly by 4)")
    
    