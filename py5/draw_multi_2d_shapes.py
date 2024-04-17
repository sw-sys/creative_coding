import py5

### Draw 2D shapes

angle = 50 # change shape rotation

def setup():
    py5.size(700, 700) # size of canvas
    py5.no_loop()  # run draw function once
    py5.background(128, 0, 128)  # Set purple background
    draw_circle()
    draw_rectangle()
    draw_triangle()

def draw_rectangle():
    global angle
    py5.translate(py5.width / 2, py5.height / 2) # coord systems origin \ horizontal line from top left
    py5.rotate(angle)
    py5.fill(0, 0, 255)  # Always blue color
    py5.rect(-50, -50, 120, 100)  # Position rect x, y and draw width, height
    angle += 0.01

def draw_circle():
    global angle
    py5.translate(py5.width /5, py5.height / 5) # coord systems origin \ horizontal line from top left
    py5.rotate(angle)
    py5.fill(0, 0, 100)  # dark blue color
    py5.circle(-50, -50, 100)  # Position circ x, y and draw size

def draw_triangle():
    global angle
    py5.translate(py5.width / 10, py5.height / 10) # coord systems origin \ horizontal line from top left
    py5.rotate(angle)
    py5.fill(100, 100, 100)  # grey color
    py5.triangle(-50, -50, -50, 100, 120, 100)  # Position x, x, y, y and z, z - one for each corner

py5.run_sketch()