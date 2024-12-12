# Leila Furman
# 31/10/24
# P4LAB2
# Create program that asks user for positive integer and displays multiplication table

# While loop to control program running continuously
run_again = "y"

while run_again == "yes" or run_again == "y":
    user_int = int(input("Enter an integer: "))
    print()
    if user_int >= 0: # Print multiplication table
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int * num}")
    else:
        print("This program does not handle negative numbers.")

    run_again = input("Would you like to run the program again? ").lower()
    valid_inputs = ["yes", "y", "no", "n"]
    # Validate the user's input
    while run_again not in valid_inputs:
        print("Invalid response entered.")
        run_again = input("Would you like to run the program again? ").lower()


# Loop breaks
print("Exiting program...")
