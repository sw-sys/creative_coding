# draw star
from turtle import *
from turtle2img import save_jpg, save_png

# cursor settings
hideturtle()
speed(0)
width(2)

#background
Screen().bgcolor("black")

# colour settings
color('black')
fillcolor('black')
begin_fill()

# drawing
while True:
    forward(300)
    left(130)
    if abs(pos()) < 1: # checks if turtle is at origin
        break

end_fill()

# save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_star_bw10")

# sustain window
mainloop()