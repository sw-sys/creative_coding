from turtle import *
from turtle2img import save_png

# Cursor settings
hideturtle()
speed(0)

# Background
Screen().bgcolor("black")

def draw_star(size, x, y):
    penup()
    goto(x, y)
    pendown()
    color("blue")
    fillcolor("red")
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()

# Set up the turtle
screen = Screen()
t = Turtle()
t.penup()

# Generate the grid of stars
for row in range(10):
    for col in range(10):
        x = -250 + col * 50
        y = 250 - row * 50
        draw_star(20, x, y)

# Save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_grid_test")

# Sustain window
done()