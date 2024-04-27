# tut https://www.youtube.com/watch?v=ojL41F1AhWc&list=PLVOI8k9AArsdF2Hizssnm9ncO513I9GSn

from turtle import *
from turtle2img import save_jpg, save_png

cursor = Turtle()
screen = Screen()
screen.bgcolor("Black") # background
cursor.speed(0) # draw speed

radius = 60 # of circle
cursor.pensize(10) # width of line
colour = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"] # draw using these colours

for x in range(12): # instructions for drawing each layer 
    cursor.color(colour[x%6])
    for i in range(6): # 0-5
        cursor.circle(radius) #draw a circle
        cursor.right(60) # rotate 60 degrees clockwise
    radius = radius + 4 # increase radius each loop

### save image
def save(file_name):
    save_png(file_name + ".png")

save("turtle_flower_rainbow")

mainloop()