# Leila Furman
# 11/7/2024
# P4HW2
# Calculate reg & OT pay, given an employee's hours worked, for multiple employees

emp_name = input("Enter employee's name or 'Done' to terminate: ")

# These are all the incrementer values
num_emps = 0
total_ot_pay = 0
total_reg_pay = 0
total_pay = 0

# This is the loop for the program
while emp_name.lower() != "done":
    num_emps += 1
    num_hours = float(input(f"How many hours did {emp_name} work? "))
    pay_rate = float(input(f"What is {emp_name}'s pay rate? "))
    print()
    print(f"{'Employee name:':<17}{emp_name}")
    print()
    if num_hours > 40:
        ot_hours = num_hours - 40
        ot_pay = ot_hours * (pay_rate * 1.5)
        reg_pay = 40 * pay_rate
        gross_pay = ot_pay + reg_pay
        total_ot_pay = total_ot_pay + ot_pay
        total_reg_pay = total_reg_pay + reg_pay
        total_pay = total_pay + gross_pay

    else: # hours worked is < or == 40
        ot_hours = 0
        ot_pay = 0
        reg_pay = num_hours * pay_rate
        gross_pay = reg_pay
        total_ot_pay = total_ot_pay + ot_pay
        total_reg_pay = total_reg_pay + reg_pay
        total_pay = total_pay + gross_pay

    print(f"{'Hours Worked':<14}{'Pay Rate':<11}{'OverTime':<13}{'OverTime Pay':<14}{'RegHour Pay':<12}{'Gross Pay'}")
    print("------------------------------------------------------------------------------")
    print(f"{num_hours:<14}{pay_rate:<11}{ot_hours:<13}{ot_pay:<14}${reg_pay:<12}${gross_pay:<12}")
    print()
    emp_name = input("Enter employee's name or 'Done' to terminate: ")

# Loop breaks, display totals
print()
print(f"Total number of employees entered: {num_emps}")
print(f"Total amount paid for overtime: ${total_ot_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_reg_pay:.2f}")
print(f"Total amount paid in gross: ${total_pay:.2f}")
