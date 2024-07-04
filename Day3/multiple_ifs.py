# if a person is <= 120m tall, then they can ride a rollercosta, else they can't
# also if they are <= 120m tall, then we check if they are under 12yrs, charge is $5, between 12 -18yrs, charge is $7 and above 18yrs charge is $12

height = int(input('Enter your height: '))
charge = 0

# Check for the height
if height > 120:
    print('You can ride the rollerCosta')
    age = int(input('Enter your age: '))
    if age < 12:
        charge = 5
        print(f'Please pay: $5')
    elif age < 18:
        charge = 7 
        print(f'Please pay: $7')
    else:
        charge = 12
        print(f'Please pay: $12')
        
    want_photo = input("Do you want a photo? Y or N: ")
    if want_photo == 'Y':
        charge = charge + 3
    
    print(f'Total Bill is ${charge}')
        
else:
    print("You can't ride the rollerCosta")
