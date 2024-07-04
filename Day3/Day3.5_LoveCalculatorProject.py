print("Welcome to Love Calculator!")
my_name = input('What is your name? \n')
their_name = input('What is their name?\n')

# Concatente the two names together
name = my_name + their_name

# Change all the name letters to lowercase
name_to_lower = name.lower()

# Count how many times each letter in word "TRUE" and "LOVE" appears in the name
t_count = name_to_lower.count("t")
r_count = name_to_lower.count("r")
u_count = name_to_lower.count("u")
e_count = name_to_lower.count("e")

l_count = name_to_lower.count("l")
o_count = name_to_lower.count("o")
v_count = name_to_lower.count("v")

# Displaying how many times the letters appear
print(f"T occurs {t_count} times")
print(f"R occurs {r_count} times")
print(f"U occurs {u_count} times")
print(f"E occurs {e_count} times")
totalCountTrue = t_count + r_count + u_count + e_count
print(f"Total    {totalCountTrue}")


print(f"L occurs {l_count} times")
print(f"O occurs {o_count} times")
print(f"V occurs {v_count} times")
print(f"E occurs {e_count} times")
totalCountLove = l_count + o_count + v_count + e_count
print(f"Total    {totalCountLove}")

# Concatenate string values of love and true totals
loveScore = str(totalCountTrue) + str(totalCountLove)

# Add comments according to the score
if int(loveScore) < 10 or int(loveScore) > 90:
    print(f"Your score is {loveScore}%, you go together like coke and mentos.")
elif int(loveScore) <= 40 and int(loveScore) >= 50:
    print(f"Your score is {loveScore}%, you are alright together.")
else:
    print(F"Your score is {loveScore}%")