# TODO: Implement A* algorithm

## Hint: You must be able to reconstruct the path once the algorithm has finished
## Hint: You must be able to visualize the algorithm in action i.e call the methods to draw on the screen to visualize the algorithm in action in the astar function
import pygame
# import typing
from queue import PriorityQueue
from components.grid import reconstruct_path
from components.spot import Spot
import dill as pickle

import sys

sys.setrecursionlimit(100000)

def h(p1: Spot, p2: Spot): # Manhattan/ taxicab distance
	"""
	Helper function to calculate the Manhattan/taxicab distance

	Args:
	- p1 (Spot): First Node 
	- p2 (Spot): Second Node

	Returns:
	- distance (float): Manhattan distance between p1 and p2
	
	"""
	x1, y1 = p1.get_pos()
	x2, y2 = p2.get_pos()

	distance = abs(x1 - x2) + abs(y1 - y2)
	return distance

def a_star_algo(draw, grid: list, start: Spot, end: Spot, test: bool = False):
	"""
	Function that implements the A* algorithm.

	Args:
	- draw (function): A function to update the grid colors.
	- grid (list): A 2D list representing the grid. Each element is an instance of the 'Spot' class.
	- start (Spot): The starting node to begin pathfinding.
	- end (Spot): The ending node where the path should end.
	- test (bool): If function used for testing, test should be True. Otherwise, False.
	
	Returns:
	- path_found (bool): True if a path is found, otherwise False.
	- count (int): Number of Nodes traversed.
	- path_len (int): Length of path. 
	"""

	# db = {}
	# db["grid"] = grid
	# db["start"] = start
	# db["end"] = end
	# print(db)
	# with open('complex2case', 'wb') as file:
	# 	pickle.dump(db, file)

	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start, end)

	open_set_hash = {start}

	while not open_set.empty():
		if test == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()


		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			path_len = reconstruct_path(came_from, end, draw) #nedit : made it equal to path_len
			end.make_end()
			start.make_start()
			path_found = True #nedit
			# print(f_score)
			return path_found, count, path_len #nedit: Original was just --> True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor, end)
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()
		if draw != None:
			draw()

		if current != start:
			current.make_closed()
	
	path_len = None #nedit
	path_found = False #nedit
	return path_found, count, path_len #none bc no path_len #nedit: Original was just --> False

# with open("simplecase", 'rb') as file:
#     db = pickle.load(file)
#     simple_grid = db["grid"]
#     simple_start = db["start"]
#     simple_end = db["end"]

# a_star_algo(None, simple_grid, simple_start, simple_end, True)