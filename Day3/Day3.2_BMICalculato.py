weight = float(input("Enter your weight: "));
height = float(input("Enter your height: "));

bmi = round((weight / (height ** 2)))

if bmi < 18.5:
    print(f"Your MBI is {bmi}, and you are Underweight")
elif bmi < 25:
    print(f"Your MBI is {bmi}, and you have a normal weight")
elif bmi < 30:
    print(f"Your MBI is {bmi}, and you are Overweight")
elif bmi < 35:
    print(f"Your MBI is {bmi}, and you are obese")
else:
    print(f"Your MBI is {bmi}, and you are clinically obese")
    