student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

# Create an empty dictionarycalled student_grades
student_grades = {}

# Write your code below to add the grades to the new dictionary

# First get all the students and their marks by looping through
for student in student_scores:
    score = student_scores[student]
    
    # Grade according to side
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        

print(student_grades)