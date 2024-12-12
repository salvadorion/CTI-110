# Leila Furman
# 10/24/2024
# P3HW2
# Calculate reg & OT pay, given an employee's hours worked

'''
input: get the name as a string
input: get the hours worked as an integer
input: get the pay rate as a float
print: a line of -'s to make it look pretty ^_^

output: print employee name

if hours worked is greater than 40:
    calculate OT hours worked by subtracting 40 from hours worked
    calculate OT pay (OT hours * pay rate * 1.5)
    calculate reg pay (40 * reg pay rate)
    calculate gross pay by adding OT pay and reg pay together
    
else: (hours worked is less than or equal to 40)
    overtime hours equals 0
    overtime pay also equals 0
    calculate reg pay (reg hours * reg pay rate)
    gross pay is just reg pay

output:
display total hours worked
display regular pay rate
display hours of overtime
display money earned from overtime ( OT hours times OT pay rate )
display money earned from regtime ( reg hours times reg pay rate )
display total money earned ( OT pay plus reg pay ) 
'''
emp_name = input("Enter employee's name: ")
num_hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("--------------------------------")
print(f"{'Employee name:':<17}{emp_name}")
print()

if num_hours > 40:
    ot_hours = num_hours - 40
    ot_pay = ot_hours * (pay_rate * 1.5)
    reg_pay = 40 * pay_rate
    gross_pay = ot_pay + reg_pay

else: # hours worked is < or == 40
    ot_hours = 0
    ot_pay = 0
    reg_pay = num_hours * pay_rate
    gross_pay = reg_pay

print(f"{'Hours Worked':<14}{'Pay Rate':<11}{'OverTime':<13}{'OverTime Pay':<14}{'RegHour Pay':<12}{'Gross Pay'}")
print("------------------------------------------------------------------------------")
print(f"{num_hours:<14}{pay_rate:<11}{ot_hours:<13}{ot_pay:<14}${reg_pay:<12}${gross_pay:<12}")
