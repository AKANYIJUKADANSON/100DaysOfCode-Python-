# ~~~~~~~~~~~~~~~~~Dictionaries use the key:value method
creatures_dictionary = {
    "Bird": "Hen, Dove, Turkey",
    "DomesticAnimals":"Goat, cow, Pig, Sheep",
    "WilAnimals": "Lion, Elephant, Cheeter"
}

# ~~~~~~~~~~~~~~~~Retrieving data ina dictionary
# print("Wild Animals Include: " + creatures_dictionary["WilAnimals"])

# ~~~~~~~~~~~~~~~~~Adding data in a dictionary
creatures_dictionary['pets'] = "Cat, Dog"

# print(creatures_dictionary)

# ~~~~~~~~~~~~~~~~~Wiping a dictionary
# creatures_dictionary = {}

# ~~~~~~~~~~~~~~~~~~Editing an item in a dictionary
# creatures_dictionary["Bird"] = "Hello, Woodie, Wekesa"
# print(creatures_dictionary)

# ~~~~~~~~~~~~~~~~~~~Looping through a dictionary
# for key in creatures_dictionary:
#     print(key)
#     print(creatures_dictionary[key]) 
    
# Using other data types as keys
students = {
    1: "Addan Sidin",
    2: "Abdelgader",
    3: "Jane",
    4: "Lilly"
}


# print(students[2])



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STUDENT GRADING SYSTEM EXERCISE

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    print(key)
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)