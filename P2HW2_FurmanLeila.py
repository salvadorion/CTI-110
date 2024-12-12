# Leila Furman
# 10/10/2024
# P2HW2
# Use lists and functions in lists

# Prompt user for grades
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

# Do the funny list variable stuff
grade_list = [mod1, mod2, mod3, mod4, mod5, mod6]

# Make the average variable </3
grade_avg = sum(grade_list)/len(grade_list)

# Display grade results
print("----------Results----------")
print(f"{'Lowest Grade: ':<18}{min(grade_list):,.2F}")
print(f"{'Highest Grade: ':<18}{max(grade_list):,.2F}")
print(f"{'Sum of Grades: ':<18}{sum(grade_list):,.2F}")
print(f"{'Average: ':<18}{grade_avg:,.2F}")
