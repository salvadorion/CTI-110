 # Leila Furman
 # 9/26/2024
 # P1HW2
 # Use Python to create a travel budget by getting input from the user

print("This program calculates and displays travel expenses")
print()

 # Get budget from user
budget = int(input("Enter Budget: "))
print()

 # Get travel destination from user
trav_dest = input("Enter your travel destination: ")
print()

 # Get gas expenses from user
gas_money = int(input("How much do you think you will spend on gas? "))
print()

 # Get accommodations expenses from user
acc_money = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
 
 # Get food expenses from user
food_money = int(input("Lastly, how much do you need for food?"))
print()

print("----------Travel Expenses----------")
# Display travel destination, budget, and expenses
print(f"Location: {trav_dest}")
print(f"Initial Budget: {budget}")
print()

print(f"Fuel: {gas_money}")
print(f"Accommodation: {acc_money}")
print(f"Food: {food_money}")
print()

# Calculate remaining balance
rem_bal = budget - (gas_money + acc_money + food_money)

# Display remaining balance
print(f"Remaining Balance: {rem_bal}")
