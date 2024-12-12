# Leila Furman
# 29/10/24
# P4LAB1
# Use loops and turtle library to draw a house

# Important turtle library
import turtle

# Set up the window and turtle object
window = turtle.Screen()
tommy = turtle.Turtle()

# Change turtle features
tommy.pensize(6)
tommy.pencolor("blue")
tommy.shape("turtle")

# While loop that runs 4 times
movement = 0

while movement <= 3:
    movement += 1
    tommy.forward(150)
    tommy.right(90)

# For loop that runs 3 times
tommy.left(60)

for side in range(3):
    tommy.forward(150)
    tommy.right(120)
