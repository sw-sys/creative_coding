from turtle import *

### cursor set up
hideturtle()
speed(0)
# width(2)

#background
Screen().bgcolor("white")

### colour settings
color('black')
fillcolor('black')
begin_fill()
### drawing start
### drawing end
end_fill()

### drawing

# save to image
def save(file_name):
    Screen().getcanvas().postscript(file=file_name + ".eps", colormode='color')

save("turtle_drawing_1")

### sustain window
mainloop()