 # Leila Furman
 # 10/1/24
 # P2LAB1
 # Using built-in libraries for circle calculations

# Import the math library
import math

# Create a variable to hold pi
pi = math.pi

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate and display the diameter
diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calculate the circumference
circumf = 2 * pi * radius

# Round variable to 2 decimal places
r_circumf = round(circumf, 2)

# Display the circumference
print(f"The circumference of the circle is {circumf:.2f}\n")
print(f"The rounded circumference of the circle is {r_circumf}\n")

# Calculate and display the area
area = math.pi * radius ** 2
print(f"The area of the circle is {area:.3f}")
