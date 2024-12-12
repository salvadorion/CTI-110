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

# Display letter grade using branching
print("------------------------------------")
letter_grade = ""

if grade_avg >= 90:
    letter_grade = "A"
elif grade_avg >= 80:
    letter_grade = "B"
elif grade_avg >= 70:
    letter_grade = "C"
elif grade_avg >= 60:
    letter_grade = "D"
else: # letter_grade less than 60
    letter_garde = "F"

print()
print(f"Your grade is: {letter_grade}")
