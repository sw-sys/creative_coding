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

def create_snowflake(length, levels):
    snowflake_side(length, levels)
    right(120)
    snowflake_side(length, levels)
    right(120)
    snowflake_side(length, levels)

create_snowflake(400, 3)

mainloop()