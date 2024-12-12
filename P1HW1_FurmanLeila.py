 # Leila Furman
 # 9/17/2024
 # P1HW1
 # Collect, process, and display information to user

print("-----Calculating Exponents-----")
print()
print()

# Get base value as an integer from the user
base_value = int(input("Enter an integer as the base value: "))

# Get exponent as an integer from the user
exponent = int(input("Enter an integer as the exponent: "))
print()
print()

# Calculate exponent
exp_result = base_value ** exponent

# Display output to the user
print(base_value,"raised to the power of",exponent,"is",exp_result,"!!")
print()
print()

print("-----Addition and Subtraction-----")
print()
print()

# Get starting integer as an integer from the user
start_int = int(input("Enter a starting integer: "))

# Get integer to add as an integer from the user
add_int = int(input("Enter an integer to add: "))

# Get integer to subtract as an integer from the user
sub_int = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate sum and difference
addsub_result = start_int + add_int - sub_int

# Display output to the user
print(start_int,"+",add_int,"-",sub_int,"is equal to",addsub_result)
