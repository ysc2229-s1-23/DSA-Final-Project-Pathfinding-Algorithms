# see https://en.wikipedia.org/wiki/Fringe_search
import pygame
from components.grid import reconstruct_path_fringe
from algorithms.a_star import h # same heuristic function
from components.spot import Spot

"-----CODE FOR FRINGE ALGORITHM------"

def fringe_algo(draw, grid: list, start: Spot, end: Spot, test: bool = False):
	"""
	Function that implements the Fringe algorithm.

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
	count = 0
	fringe = [start]
	cache = {}
	cache[start] = (0, None)
	f_limit = h(start, end)

	while fringe:
		if test == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

		f_min = float("inf")

		for node in fringe:
			g, _ = cache[node]
			f = g + h(node, end)

			if f > f_limit:
				f_min = min(f, f_min)
				continue

			if node.is_end():
				f_limit = f_min
				path_len = reconstruct_path_fringe(cache, end, draw)
				end.make_end()
				start.make_start()
				path_found = True
				return path_found, count, path_len
			if test == False:
				draw()

			if node != start:
				node.make_closed()

			for child in node.neighbors:
				g_child = g + 1

				if child in cache and cache[child] is not None:
					if g_child >= cache[child][0]:
						continue

				if child not in fringe:
					fringe.append(child)

				cache[child] = (g_child, node)

				if not child.is_start() and not child.is_end():
					count += 1
					child.make_closed()

			fringe.remove(node)  # mark as closed

		f_limit = f_min

	path_len = None 
	path_found = False 
	return path_found, count, path_len 
