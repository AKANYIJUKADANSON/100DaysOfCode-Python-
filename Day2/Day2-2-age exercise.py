max_months = 90 * 12
max_weeks = 90 * 52
max_days = 90 * 365
# Prompt user to enter their age
age = int(input("Enter your age: "))
# Days left
curr_days = 365 * age
curr_days_left = max_days - curr_days
# Weeks left
curr_weeks = 52 * age
curr_weeks_left = max_weeks - curr_weeks
# Months left
curr_months = 12 * age
curr_months_left = max_months - curr_months

print(f"You have {curr_days_left}, {curr_weeks_left} weeks, and {curr_months_left} months left.")