from turtle import *
from PIL import Image

shape("turtle")
speed(0) # 0 is fast

def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def create_snowflake(sides, length):
    colors = ["blue", "lightblue", "darkblue", "blue", "lightblue", "darkblue"]
    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)

create_snowflake(3, 300)

mainloop()