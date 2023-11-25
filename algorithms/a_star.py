# TODO: Implement A* algorithm

## Hint: You must be able to reconstruct the path once the algorithm has finished
## Hint: You must be able to visualize the algorithm in action i.e call the methods to draw on the screen to visualize the algorithm in action in the astar function
import pygame
from queue import PriorityQueue
from components.grid import reconstruct_path

def h(p1, p2): # Manhattan/ taxicab distance
	"""
	Helper function to calculate the Manhattan/taxicab distance

	Args:
	- p1 (tuple): position containing x and y coordinates
	- p2 (tuple): position containing x and y coordinates

	Output:
	- distance (float): Manhattan distance between p1 and p2
	
	"""
	x1, y1 = p1.get_pos()
	x2, y2 = p2.get_pos()

	distance = abs(x1 - x2) + abs(y1 - y2)
	return distance

def a_star_algo(draw, grid, start, end):
	"""
	Function that implements the A* algorithm

	Args:
	- draw :
	- grid :
	- start :
	- end :
	
	"""

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
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			return True

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

		draw()

		if current != start:
			current.make_closed()

	return False