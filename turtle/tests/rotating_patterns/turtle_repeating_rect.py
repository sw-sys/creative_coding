import turtle
from turtle2img import save_jpg, save_png

turtle.bgcolor("White")

cursor = turtle.Turtle()
cursor.speed(0)
cursor.pencolor("Blue")
cursor.hideturtle()

colour=["Blue", "Dark Blue", "Black"]


for i in range(400):
    cursor.color(colour[i%3])
    cursor.forward(i)
    cursor.left(91)

### save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_repeating_rect")

turtle.mainloop()