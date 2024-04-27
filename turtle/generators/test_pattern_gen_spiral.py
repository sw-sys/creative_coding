from turtle import *
from turtle2img import save_jpg, save_png

### color schemes
# rainbow '#FF6D6A', '#EFBE7D','#E9EC6B','#C1F0B2', '#8BD3E6', '#B1A2CA'
# blues '#95C8D8', '#B0E0E6', '#8AB9F1', '#034694', '#0F52BA', '#000080', '#003151'
# neutrals '#FDE992', '#F4A460', '#E8CAA2', '#D1AF90', '#DCD7A0', '#B37959', '#856D4D'

# cursor settings
hideturtle()
speed(0)
width(10)

# bkgd settings
Screen().bgcolor("white")

# drawing
for steps in range(250):
    for c in ('#FDE992', '#F4A460', '#E8CAA2', '#D1AF90', '#DCD7A0', '#B37959', '#856D4D'):
        color(c)
        forward(steps)
        right(15)

### save image - test
def save(file_name):
    save_png(file_name + ".png")

save(r"spirals\turtle_spiral_neutral_fossil_gradient_15_250")

# # save to image - colour
# def save(file_name):
#     Screen().getcanvas().postscript(file=file_name, colormode='color')

# save(r"spirals\turtle_spiral_neutral_gradient_.eps")

# sustain window
mainloop()