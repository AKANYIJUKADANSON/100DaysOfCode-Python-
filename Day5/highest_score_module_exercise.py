# 78 65 89 86 55 91 64 89

student_score = input('Enter a list of scores seperated by space: ').split()

max_score = 0
for score in student_score:
    if int(score) > max_score:
        max_score = int(score)
        
print(f"The highest score is: {max_score}")