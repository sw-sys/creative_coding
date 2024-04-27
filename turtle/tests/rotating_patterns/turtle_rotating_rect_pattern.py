from turtle import *

cursor = Turtle()
screen = Screen()
screen.bgcolor("Black") # background
cursor.speed(0) # draw speed

side_length = 100 # length of the side of the rectangle
cursor.pensize(2) # width of line
colour = ["Red", "Magenta", "Blue"] # draw using these colours

cursor.color(colour[1])
for i in range(6): # 0-5
    for j in range(4): # draw a rectangle
        cursor.forward(side_length)
        cursor.left(90)
    cursor.right(60) # rotate 60 degrees clockwise

mainloop()