 # Leila Furman
 # 9/26/2024
 # P1HW2
 # Edit and enhance a Python program (P1HW2)

print("This program calculates and displays travel expenses")
print()

 # Get budget from user
budget = float(input("Enter Budget: "))
print()

 # Get travel destination from user
trav_dest = input("Enter your travel destination: ")
print()

 # Get gas expenses from user
gas_money = float(input("How much do you think you will spend on gas? "))
print()

 # Get accommodations expenses from user
acc_money = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
 
 # Get food expenses from user
food_money = float(input("Lastly, how much do you need for food? "))
print()

print("----------Travel Expenses----------")
# Display travel destination, budget, and expenses
print(f"{'Location:':<18}{trav_dest}")
print(f"{'Initial Budget:':<18}${budget:,.2F}")
print(f"{'Fuel:':<18}${gas_money:,.2F}")
print(f"{'Accommodation:':<18}${acc_money:,.2F}")
print(f"{'Food:':<18}${food_money:,.2F}")

# Calculate remaining balance
rem_bal = budget - (gas_money + acc_money + food_money)

print("-----------------------------------")
print()
# Display remaining balance
print(f"Remaining Balance: ${rem_bal:,.2F}")
