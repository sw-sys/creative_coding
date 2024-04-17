import py5

def setup():
    py5.size(500, 500)
    py5.background(255)

def draw():
    py5.stroke(0)
    py5.fill(128)
    
    # Draw a circle in the center of the canvas
    py5.circle(250, 250, 100)
    
    # Use control flow to change the color of the circle based on mouse position
    if py5.mouse_x < 250 and py5.mouse_y < 250:
        py5.fill(255, 0, 0)  # Red if mouse is in top-left quadrant
    elif py5.mouse_x >= 250 and py5.mouse_y < 250:
        py5.fill(0, 255, 0)  # Green if mouse is in top-right quadrant
    elif py5.mouse_x < 250 and py5.mouse_y >= 250:
        py5.fill(0, 0, 255)  # Blue if mouse is in bottom-left quadrant
    else:
        py5.fill(255, 255, 0)  # Yellow if mouse is in bottom-right quadrant
    
    py5.circle(250, 250, 100)

py5.run_sketch()