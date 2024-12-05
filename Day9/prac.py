teachers = {'Racheal': "English", "Veron": "Computer Science", "Prossy": "Mathematics"}

# Number of items in the dictionary
# print(f"Number of items: {len(teachers)}")
# print(f"Data type of items: {type(teachers)}")

subject = input("Enter subject to find the teacher: ")

winner = list(teachers.keys())[list(teachers.values()).index(subject)]

print(f"Tr. {winner}")