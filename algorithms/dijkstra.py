#TODO: Implement the dijkstra algorithm

## Hint: You must be able to reconstruct the path once the algorithm has finished
## Hint: You must be able to visualize the algorithm in action i.e call the methods to draw on the screen to visualize the algorithm in action in the dijkstra function

import pygame
import heapq
from components.grid import reconstruct_path

def dijkstra_algo(draw, grid, start, end):
	distances = {spot: float("inf") for row in grid for spot in row}
	distances[start] = 0  # Set the distance of the start vertex to zero
	priority_queue = [(0, start)]
	came_from = {}
	# visited = set()

	while priority_queue:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = heapq.heappop(priority_queue)[1]

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			return True

		for neighbor in current.neighbors:
			distance = distances[current] + 1
			if distance < distances[neighbor]:
				came_from[neighbor] = current
				distances[neighbor] = distance
				heapq.heappush(priority_queue, (distance, neighbor))
				neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False