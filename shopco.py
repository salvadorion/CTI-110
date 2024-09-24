# Leila Furman
# 9/24/2024
# In-Class Example
# Simulate shopping for 3 items and receipt

print("Welcome to ShopCo!\n")
print("You are going to purchase three items.")

# Get item1 info from user
item1 = input("Enter name of first item: ")
price1 = float(input(f"Enter the price of {item1}: "))
quantity1 = int(input(f"Enter the quantity of {item1}: "))
print()
# Get item2 info from user
item2 = input("Enter name of second item: ")
price2 = float(input(f"Enter the price of {item2}: "))
quantity2 = int(input(f"Enter the quantity of {item2}: "))
print()
# Get item3 info from user
item3 = input("Enter name of third item: ")
price3 = float(input(f"Enter the price of {item3}: "))
quantity3 = int(input(f"Enter the quantity of {item3}: "))
print()

print("----------ShopCo Receipt----------\n\n")
print(f"{item1}      {quantity1}     ${price1 * quantity1:.2f}\n")
print(f"{item2}      {quantity2}     ${price2 * quantity2:.2f}\n")
print(f"{item3}      {quantity3}     ${price3 * quantity3:.2f}\n")
print("-----------------------------------\n\n")

# Calculate subtotal
subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

# Calculate tax
tax_owed = 0.07 * subtotal

# Calculate final total owed
total_owed = subtotal + tax_owed

# Display subtotal, tax, and final total
print(f"Subtotal:     ${subtotal:.2f}\n")
print(f"Tax Owed:     ${tax_owed:.2f}\n\n")
print(f"TOTAL:        ${total_owed:.2f}")
