import pygame
from algorithms.a_star import h # same heuristic function
from queue import PriorityQueue
from components.spot import Spot


"-----MEMORIAL: NOT USED OR FAILED FUNCTIONS-------"

#code temporarily put in algorithm function to save grid configurations (found in test_grids folder).
# db = {}
# db["grid"] = grid
# db["start"] = start
# db["end"] = end
# print(db)
# with open('complex2case', 'wb') as file:
# 	pickle.dump(db, file)

#Incomplete IDA* Functions
def reconstruct_path_IDA(path: list[Spot], draw):
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

def ida_star_algo(draw, grid, start, end):
	"""
	Implements the IDA* search algorithm.

	Args:
		grid (Grid): An object representing the current grid

	Returns:
		None
	"""
	bound = h(start, end)

	# Stack for path being searched
	path = [start]

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		result = search(draw, path, 0, bound, end)

		if result == True:
			path.reverse()
			reconstruct_path_IDA(path, draw)
			return True
		elif result == float("inf"):
			return False

		bound = result

def successor(node, g, h, end):
	ordered = PriorityQueue()
	for neighbor in node.neighbors:
		ordered.put((g+h(node, end), neighbor))
	list = []
	while ordered:
		list.append(ordered.get()[1])
	return list

def search(draw: object, path: list, g: int, bound: float, end: object):
	"""
	Recursive search function used by the IDA* algorithm.

	Args:
	- draw (function): The draw function to update the grid display.
	- path (list): The list of nodes representing the path taken by the search algorithm.
	- g (int): The cost of the path represented by the list of nodes.
	- bound (float): The bound on the cost of the path.
	- end (Node): The ending node.
	
	Returns:
	- True (bool): end was reached
	- f (float): g-score + heuristic is greater than current depth (bound)
	- min_val (float): minimum value for the path
	"""
	# Get last node in path
	node = path[-1]

	# Calculate the f-score
	f = g + h(node, end)

	if f > bound:
		return f
	elif node.is_end():
		return True

	# if not node.is_start() and not node.is_end():
	# 	node.make_open()
	# draw()
	# if not node.is_start() and not node.is_end():
	# 	node.make_closed()

	min_val = float("inf")
	for neighbor in successor(node, g, h, end):
		if neighbor not in path:
			if not neighbor.is_start() and not neighbor.is_end():
				neighbor.make_open()

			path.append(neighbor)
			result = search(draw, path, g + 1, bound, end)

			if result is True:
				return True
			elif result < min_val:
				min_val = result

			path.pop()
	draw()
	if not node.is_start() and not node.is_end():
		node.make_closed()
	return min_val