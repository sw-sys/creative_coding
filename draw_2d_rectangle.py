import py5

### Draw 2D square

angle = 50 # change shape rotation

def setup():
    py5.size(500, 400) # size of canvas
    py5.no_loop()  # run draw function once
    py5.background(128, 0, 128)  # Set purple background
    draw_rectangle()

def draw_rectangle():
    global angle
    py5.translate(py5.width / 3, py5.height / 3) # coord systems origin \ horizontal line from top left
    py5.rotate(angle)
    py5.fill(0, 0, 255)  # Always blue color
    py5.rect(-50, -50, 120, 100)  # Position rect x, y and draw width, height
    angle += 0.01

py5.run_sketch()