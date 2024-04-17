from turtle import *

pointer = shape("turtle")

def instructions():
    global pointer
    speed(0) # make turtle as fast as light
    forward(100)
    left(45) # turn left
    forward(100)
    right(90) # turn right
    forward(100)
    right(45)
    backward(100)

instructions()

#keep window open
mainloop()