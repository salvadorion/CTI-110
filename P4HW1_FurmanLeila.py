# Leila Furman
# 11/5/2024
# P4HW1
# Use loops to create a program for collecting and evaluating scores

# Get number of scores user would like to enter
numScores = int(input("How many scores do you want to enter? "))

# Create a list to hold valid inputs
grades = []

# For loop to iterate (numScores) times
for score in range(numScores):
    userInput = int(input(f"Enter score #{score+1}: "))
    while userInput < 0 or userInput > 100:
        print("INVALID score entered!!")
        print("Score should be between 0 and 100")
        userInput = int(input(f"Enter score #{score+1} again: "))
    # Once valid score is given, add it to the list
    grades.append(userInput)

print()
print()
print("----------Results-----------")
# Calculate & display lowest score 
lowestScore = min(grades)
print(f"Lowest Score  : {lowestScore:.1f}")

# Remove the lowest grade from the list, display new list
grades.remove(lowestScore)
print(f"Modified List : {grades}")

# Get and display average from new list 
average = sum(grades) / len(grades)
print(f"Scores Average: {average:.2f}")

# Get and display letter grade from new list
if average >= 90:
    letterGrade = "A"
elif average >= 80:
    letterGrade = "B"
elif average >= 70:
    letterGrade = "C"
elif average >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"
print(f"Grade         : {letterGrade}")
