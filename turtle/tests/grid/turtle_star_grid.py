from turtle import *
from turtle2img import save_png

# Background
Screen().bgcolor("black")

def draw_star(size, x, y):
    penup()
    goto(x, y)
    pendown()
    color("orange")
    fillcolor("yellow")
    begin_fill()
    for i in range(5):
        forward(size)
        right(100)
    end_fill()

# Set up the turtle
screen = Screen()
penup()
hideturtle()
speed(0)

# Generate the grid of stars
for row in range(10):
    for col in range(10):
        x = -250 + col * 50
        y = 250 - row * 50
        draw_star(20, x, y)

# save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_star_grid")

# Sustain window
done()