import py5

# draws a grid, black stroke (outlines)

def setup():
    py5.size(500, 500)
    py5.background(255)

def draw():
    grid_size = 10  # Number of rows and columns in the grid
    cell_size = py5.width / grid_size  # Calculate the size of each cell

    for row in range(grid_size):
        for col in range(grid_size):
            x = col * cell_size
            y = row * cell_size
            py5.rect(x, y, cell_size, cell_size)

py5.run_sketch()