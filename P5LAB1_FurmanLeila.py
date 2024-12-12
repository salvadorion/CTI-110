# Leila Furman
# 11/14/2024
# P5LAB1
# Calculate coin combinations & simulate using self-checkout machine

import random

def calcCashBack():
    # Generate a random float for amount owed to store
    totalOwed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${totalOwed:.2f}")
    cash = float(input("How much cash will you put in the self-checkout? "))
    cashBack = cash - totalOwed
    return cashBack


    
def disperseCashBack(change):

    # Convert the float value into an integer
    change = int(round(change * 100, 2))
    
    if change == 0:
        print("No Change Due")
        
    if change > 0:
        # Calculate the amount of dollars + remove them from money variable
        num_dollars = change // 100
        # print(f"Dollars: {num_dollars}")
        change = change - (num_dollars * 100)

        # Calculate the amount of quarters + remove them from money variable
        num_qrtrs = change // 25
        # print(f"Quarters: {num_qrtrs}")
        change = change - (num_qrtrs * 25)

        # Calculate the amount of dimes + remove them from the money variable
        num_dimes = change // 10
        # print(f"Dimes: {num_dimes}")
        change = change - (num_dimes * 10)

        # Calculate the amount of nickels + remove them from the money variable
        num_nickels = change // 5
        # print(f"Nickels: {num_nickels}")
        change = change - (num_nickels * 5)

        # Calculate the amount of pennies + remove them from the money variable
        num_pennies = change
        # print(f"Pennies: {num_pennies}")
        change = change - num_pennies
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
        


    # Calculate the amount of each coin needed
    # Integer division - //

# Define the main
def main():
    print("Self-checkout machine moment")
    print()
    cash_back = calcCashBack()
    print(f"Change is: ${cash_back:.2f}")
    print()
    disperseCashBack(cash_back)
    

# Call the main
if __name__ == "__main__":
    main()
