# if a person is <= 120m tall, then they can ride a rollercosta, else they can't
# also if they are <= 120m tall, then we check if they are 18 or above to charge them accordingly. 18 and below yrs <= $7, 19 and above = $10

height = int(input('Enter your height: '))

# Check for the height
if height > 120:
    print('You can ride the rollerCosta')
    age = int(input('Enter your age: '))
    if age <= 18:
        print(f'Your charge is: $7')
    else:
        print(f'Your charge is: $10')
else:
    print("You can't ride the rollerCosta")