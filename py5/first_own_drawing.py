import py5

def setup():
    py5.size(800, 800)
    py5.background('#FF0000')
    draw_circle1()
    draw_circle2()
    draw_circle3()

def draw_circle1():
    py5.circle(100, 100, 100)
    py5.fill(0, 0, 255) # white

def draw_circle2():
    py5.circle(200, 200, 200)
    py5.fill(355, 0, 255) # royal blue

def draw_circle3():
    py5.circle(400, 400, 400)
    py5.fill(655, 0, 255) # royal blue

py5.run_sketch()