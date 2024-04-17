import py5

def setup():
    py5.size(1000, 1000)
    py5.background(0, 0, 0)

def draw():
    py5.circle(100, 100, 100)
    py5.fill(128, 128, 128)
    py5.circle(150, 200, 150)
    py5.fill(96, 96, 96)
    py5.circle(300, 300, 200)
    py5.fill(64, 64, 64)
    py5.circle(600, 400, 400)

py5.run_sketch()