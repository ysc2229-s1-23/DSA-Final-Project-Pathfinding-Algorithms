#TODO: Implement the dijkstra algorithm

## Hint: You must be able to reconstruct the path once the algorithm has finished
## Hint: You must be able to visualize the algorithm in action i.e call the methods to draw on the screen to visualize the algorithm in action in the dijkstra function

import pygame
from queue import PriorityQueue
from components.grid import reconstruct_path
from components.spot import Spot

def dijkstra_algo(draw, grid: list, start: Spot, end: Spot, test: bool = False):
	"""
	Function that implements the Dijkstra algorithm.

	Args:
	- draw (function): A function to update the grid colors.
	- grid (list): A 2D list representing the grid. Each element is an instance of the 'Spot' class.
	- start (Spot): The starting node to begin pathfinding.
	- end (Spot): The ending node where the path should end.
	
	Returns:
	- path_found (bool): True if a path is found, otherwise False.
	- count (int): Number of Nodes traversed.
	- path_len (int): Length of path. 
	"""
	distances = {spot: float("inf") for row in grid for spot in row}
	distances[start] = 0  # Set the distance of the start vertex to zero
	priority_queue = PriorityQueue()
	priority_queue.put((0, 0, start))
	count = 0 # entry count to break ties in queue, since Spot objects incomparable
	came_from = {}
	# visited = set()

	while priority_queue:
		if test == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

		current = priority_queue.get()[2]

		if current == end:
			path_len = reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			path_found = True #nedit
			return path_found, count, path_len #nedit: Original was just --> True

		for neighbor in current.neighbors:
			distance = distances[current] + 1
			if distance < distances[neighbor]:
				came_from[neighbor] = current
				distances[neighbor] = distance
				count += 1
				priority_queue.put((distance, count, neighbor))
				neighbor.make_open()
		
		if test == False:
			draw()

		if current != start:
			current.make_closed()

	path_len = None #nedit
	path_found = False #nedit
	return path_found, count, path_len #none bc no path_len #nedit: Original was just --> False