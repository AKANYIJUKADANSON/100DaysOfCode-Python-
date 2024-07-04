students_heights = input("Enter a list of student heights ").split()
count = 0
total = 0
for student in students_heights:
    count = count + 1
    total = total + int(student)
print(students_heights)

print(f"Items: {count}")
print(f"Total height: {total}")
average = total / count
print(f"Average height is: {average}")


