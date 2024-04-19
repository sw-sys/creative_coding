from turtle import *
from turtle2img import save_jpg, save_png

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

### save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_image_1")

### sustain window
mainloop()