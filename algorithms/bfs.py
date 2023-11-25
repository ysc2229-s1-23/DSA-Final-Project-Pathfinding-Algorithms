import pygame
from components.grid import reconstruct_path
from collections import deque

def bfs_algo(draw, grid, start, end):
	"""
	Function that implements the BFS algorithm.

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
	count = 0
	queue = deque([start])
	came_from = {}
	visited = set([start])

	while queue:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = queue.popleft()

		if current == end:
			path_len = reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			path_found = True #nedit
			return path_found, count, path_len #nedit: Original was just --> True

		for neighbor in current.neighbors:
			if neighbor not in visited:
				count += 1
				visited.add(neighbor)
				came_from[neighbor] = current
				queue.append(neighbor)
				neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	path_len = None #nedit
	path_found = False #nedit
	return path_found, count, path_len #none bc no path_len #nedit: Original was just --> False