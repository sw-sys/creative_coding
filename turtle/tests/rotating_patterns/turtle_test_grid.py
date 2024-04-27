from turtle import *
from turtle2img import save_jpg, save_png

# Cursor settings
hideturtle()
speed(0)

def draw_star(size, angle):
    color("black")
    fillcolor("black")
    penup()
    forward(size)
    pendown()
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()
    penup()
    backward(size)
    left(angle)

# Set up the turtle
screen = Screen()
screen.bgcolor("white")
t = Turtle()
t.color("blue")
t.penup()

# Generate the grid of stars
for angle in range(0, 360, 10):
    t.goto(0, 0)
    draw_star(50, angle)

# save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_star_grid_3")

# Sustain window
done()