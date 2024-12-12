# Leila Furman
# 10/17/2024
# P3LAB
# Calculate coin combinations for given value

'''
# Regular Division
print(100/3)

# Floor Division
print(100//3)

# Modulus Division
print(100%3)
print(7%4)
'''

# Get money value from user
money = float(input("Enter the amount of money as a float: $"))

# Check for no money & debt
if money == 0:
    print("No change")
if money < 0:
    print("You are in debt :(")

if money > 0:

    # Convert money to a whole number
    money = int(round(money * 100))

    # Calculate the amount of dollars + remove them from money variable
    num_dollars = money // 100
    # print(f"Dollars: {num_dollars}")
    money = money - (num_dollars * 100)

    # Calculate the amount of quarters + remove them from money variable
    num_qrtrs = money // 25
    # print(f"Quarters: {num_qrtrs}")
    money = money - (num_qrtrs * 25)

    # Calculate the amount of dimes + remove them from the money variable
    num_dimes = money // 10
    # print(f"Dimes: {num_dimes}")
    money = money - (num_dimes * 10)

    # Calculate the amount of nickels + remove them from the money variable
    num_nickels = money // 5
    # print(f"Nickels: {num_nickels}")
    money = money - (num_nickels * 5)

    # Calculate the amount of pennies + remove them from the money variable
    num_pennies = money
    # print(f"Pennies: {num_pennies}")
    money = money - num_pennies
else:
    num_dollars = 0
    num_qrtrs = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies =  0

# Print dollar amount grammatically correct
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else: # variable greater than 1
        print(f"{num_dollars} Dollars")

# Print quarter amount grammatically correct
if num_qrtrs > 0:
    if num_qrtrs == 1:
        print(f"{num_qrtrs} Quarter")
    else: # variable greater than 1
        print(f"{num_qrtrs} Quarters")

# Print dime amount grammatically correct
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else: # variable greater than 1
        print(f"{num_dimes} Dimes")

# Print nickel amount grammatically correct
if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else: # variable greater than 1
        print(f"{num_nickels} Nickels")

# Print penny amount grammatically correct
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else: # variable greater than 1
        print(f"{num_pennies} Pennies")
