import pygame
from components.spot import Spot
from components.constants import GREY, WHITE

def reconstruct_path(came_from, current, draw):
	"""
	Function to visualize the shortest path.

	Args:
	- came_from (dict): Dictionary containing the nodes of the shortest path.
	- current (Spot): Node to begin constructing the path from.
	- draw (function): A function to update the visualization.

	Returns:
	- Changes all the path nodes to PURPLE (color of path).
	"""
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def reconstruct_path_fringe(came_from, current, draw):
	"""
	Function to visualize the shortest path. (For Fringe Algo)

	Args:
	- came_from (dict): Dictionary containing the nodes of the shortest path.
	- current (Spot): Node to begin constructing the path from.
	- draw (function): A function to update the visualization.

	Returns:
	- Changes all the path nodes to PURPLE (color of path).
	"""
	while current in came_from:
		current = came_from[current][1]
		if current:
			current.make_path()
		draw()

def make_grid(rows, width):
	"""
	Function to create a grid for display.

	Args:
	- rows (int): Number of grid rows.
	- width (int): Width of the grid.

	Returns:
	- grid (list): A 2D list representing the grid. Each element is an instance of the 'Spot' class.
	"""
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


def draw_grid(win, rows, width):
	"""
	Function to draw grid lines on the display grid.

	Args:
	- win (pygame.Surface): The display grid to draw on.
	- rows (int): Number of grid rows.
	- width (int): Width of the grid.

	Returns:
	- None
	
	Draws appropriately spaced grid lines on the grid to distinguish each node.
	"""
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
	"""
	Function that updates the grid noting the colors of selected nodes.

	Args:
	- win (pygame.Surface): The display grid to draw on.
	- grid (list): A 2D list representing the grid. Each element is an instance of the 'Spot' class.
	- rows (int): Number of grid rows.
	- width (int): Width of the grid.

	Returns:
	- None
	"""
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win) #draws the node on the grid.

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	"""
	Function to obtain the row and column numbers of a node on the grid.

	Args:
	- pos (tuple) : Tuple containing the y and x coordinates of the position.
	- rows (int): Number of grid rows.
	- width (int): Width of the grid.

	Returns:
	- row (int): Row number of node.
	- col (int): Column number of node.
	
	"""
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

# class Grid:
    
#     # TODO:

#     ## Implement the class of the grid
#     ## You must be able to create a grid 
#     ## You must be able to draw the grid
#     ## You must be able to reset the grid
#     ## You must be able to click on the nodes of the grid
#     ## You must also need to implement a method to update the neighbors of each node which builds on top of the previous TODO
    
#     pass 