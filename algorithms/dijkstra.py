import pygame
from queue import PriorityQueue
from components.grid import reconstruct_path
from components.spot import Spot

"-----CODE FOR DIJKSTRA ALGORITHM------"

def dijkstra_algo(draw, grid: list, start: Spot, end: Spot, test: bool = False):
	"""
	Function that implements the Dijkstra algorithm.

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
	distances = {spot: float("inf") for row in grid for spot in row}
	distances[start] = 0  # Set the distance of the start vertex to zero
	priority_queue = PriorityQueue()
	priority_queue.put((0, 0, start))
	count = 0 # entry count to break ties in queue, since Spot objects incomparable
	came_from = {}
	# visited = set()

	while priority_queue.qsize() > 0:
		if test == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

		current = priority_queue.get()[2]
		

		if current == end:
			path_len = reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			path_found = True 
			return path_found, count, path_len 
		
		# print(current.neighbors)
		# non_closed_neighbors = []
		# for neighbor in current.neighbors:
		# 	if not neighbor.is_closed():
		# 		non_closed_neighbors.append(neighbor)
		# print("nonclosed")
		# print(non_closed_neighbors)

		for neighbor in current.neighbors:
			if neighbor.is_closed():
				continue
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

	path_len = None 
	path_found = False 
	
	return path_found, count, path_len 