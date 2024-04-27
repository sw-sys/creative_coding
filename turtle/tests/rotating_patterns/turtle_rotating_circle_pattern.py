# tut https://www.youtube.com/watch?v=ojL41F1AhWc&list=PLVOI8k9AArsdF2Hizssnm9ncO513I9GSn

from turtle import *

cursor = Turtle()
screen = Screen()
screen.bgcolor("Black") # background
cursor.speed(0) # draw speed

radius = 60 # of circle
cursor.pensize(2) # width of line
colour = ["Red", "Magenta", "Blue"] # draw using these colours

cursor.color(colour[1])
for i in range(6): # 0-5
    cursor.circle(radius) #draw a circle
    cursor.right(60) # rotate 60 degrees clockwise

mainloop()