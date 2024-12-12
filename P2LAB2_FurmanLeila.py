# Leila Furman
# 10/3/2024
# P2LAB2
# Using dictionary with user input

# Create the dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Get the keys only
keys = cars.keys()
print(keys)
print()

# Prompt the user to give one of the keys
user_choice = input("Enter a vehicle to see its mpg: ")
print()

# Show user mpg for their selected key
user_value = cars[user_choice]
print(f"The {user_choice} gets {user_value} mpg.")
print()

# Get amount of miles to be driven
miles = float(input(f"How many miles will you drive the {user_choice}? "))
print()

# Calculate gallons needed to drive distance
gallons_needed = miles/cars[user_choice]

# Display gallons needed to user
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {user_choice} {miles} miles.")
