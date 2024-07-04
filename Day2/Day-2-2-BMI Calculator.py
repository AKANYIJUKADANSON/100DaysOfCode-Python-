
#                   Weight
# BodyMasIndex =   __________
#                   height^2

body_weight = input("Enter your body weight: ")
body_height = input("Enter your body height: ")

BMI = int(body_weight) / (float(body_height) **2)

print(int(BMI))