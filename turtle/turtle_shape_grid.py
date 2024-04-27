from turtle import *
from turtle2img import save_png

# Background
Screen().bgcolor("black")

def draw_shape(size, x, y):
    penup()
    goto(x, y)
    pendown()
    pencolor("white")
    for i in range(1):
        for c in ('#FDE992', '#F4A460', '#E8CAA2', '#D1AF90', '#DCD7A0', '#B37959', '#856D4D'):
            color(c)
            forward(200)
            right(25)
    # color("orange")
    # fillcolor("yellow")
    # begin_fill()
    # for i in range(5):
    #     forward(size)
    #     right(144)
    # end_fill()

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
        draw_shape(30, x, y)

# ### save image - b&w test
# def save(file_name):
#     save_png(file_name + ".png")

# save(r"grid\turtle_square_grid_test")

### save to image - colour
def save(file_name):
    Screen().getcanvas().postscript(file=file_name, colormode='color')

save(r"lines\turtle_grid_1.eps")

# Sustain window
done()