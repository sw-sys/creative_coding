import py5

def seed():
    py5.random_seed(123)

# create canvas
def setup():
    py5.size(400,400)
    seed()
    py5.no_loop()

def draw():
    py5.stroke_weight(3)
    # face
    py5.fill('#F00')
    py5.circle(py5.width/2, py5.height/2, 300)
    # eyes
    py5.circle(160,150, py5.random(50,150))
    py5.circle(py5.width-160, 150, py5.random(50,150))

py5.run_sketch()