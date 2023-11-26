import pygame
from components.spot import Spot
from components.constants import GREY, WHITE
from typing import List

"------HELPER FUNCTIONS--------"

def reconstruct_path(came_from: dict, current: Spot, draw):
	"""
	Function to visualize the shortest path.

	Args:
	- came_from (dict): Dictionary containing the nodes of the shortest path.
	- current (Spot): Node to begin constructing the path from.
	- draw (function): A function to update the visualization.

	Returns:
	- path_len (int): Length of the path (number of nodes).
	Changes all the path nodes to PURPLE (color of path).
	"""
	path_len = 0 #nedit
	while current in came_from:
		path_len += 1 #nedit
		current = came_from[current]
		current.make_path()
		if draw != None:
			draw()
		# draw()

	return path_len
	

def reconstruct_path_fringe(came_from: dict, current: Spot, draw):
	"""
	Function to visualize the shortest path. (For Fringe Algo)

	Args:
	- came_from (dict): Dictionary containing the nodes of the shortest path.
	- current (Spot): Node to begin constructing the path from.
	- draw (function): A function to update the visualization.

	Returns:
	- path_len (int): Length of the path (number of nodes).
	Changes all the path nodes to PURPLE (color of path).
	"""
	path_len = 0 #nedit
	while current in came_from:
		current = came_from[current][1]
		if current:
			current.make_path()
			path_len += 1 #nedit
		if draw != None:
			draw()
	return path_len

def reconstruct_path_IDA(path: List[Spot], draw):
	"""
	Function to visualize the shortest path. (For IDA Algo)

	Args:
	- path (list[Spot])
	- draw (function): A function to update the visualization.

	Returns:
	- path_len (int): Length of the path (number of nodes).
	Changes all the path nodes to PURPLE (color of path).
	"""
	path_len = 0 
	for node in path:
		path_len += 1 
		if not node.is_start() and not node.is_end():
			node.make_path()
			draw()
	return path_len

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
	Function that updates the grid noting the colors of nodes.

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
			spot.draw(win) #draws the node color on the grid.

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