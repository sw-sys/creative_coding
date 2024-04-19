from turtle import *

# cursor settings
speed(0)
width(15)

# bkgd settings
Screen().bgcolor("black")

# drawing
for steps in range(250):
    for c in ('white', 'black'):
        color(c)
        forward(steps)
        right(15)

# save to image
def save(file_name):
    Screen().getcanvas().postscript(file=file_name, colormode='color')

save("turtle_drawing_15-degrees_250-turns_WIDTH15_bkg-black_linesW.eps")

# sustain window
mainloop()