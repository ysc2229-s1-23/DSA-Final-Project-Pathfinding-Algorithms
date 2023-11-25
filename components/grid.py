import pygame
from components.spot import Spot
from components.constants import GREY, WHITE

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def reconstruct_path_fringe(came_from, current, draw):
	while current in came_from:
		current = came_from[current][1]
		if current:
			current.make_path()
		draw()

def reconstruct_path_IDA(path, draw):
	for node in path:
		if not node.is_start() and not node.is_end():
			node.make_path()
			draw()

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
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