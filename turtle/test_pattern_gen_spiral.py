from turtle import *

Screen().bgcolor("red")
width(5)

for steps in range(400):
    for c in ('white', 'black'):
        color(c)
        forward(steps)
        right(30)

def save(file_name):
    Screen().getcanvas().postscript(file=file_name, colormode='color')

save("turtle_drawing_400.eps")

mainloop()