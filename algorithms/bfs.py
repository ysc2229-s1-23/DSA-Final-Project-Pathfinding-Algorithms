import pygame
from components.grid import reconstruct_path
from collections import deque

def bfs_algo(draw, grid, start, end):
	queue = deque([start])
	came_from = {}
	visited = set([start])

	while queue:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = queue.popleft()

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			return True

		for neighbor in current.neighbors:
			if neighbor not in visited:
				visited.add(neighbor)
				came_from[neighbor] = current
				queue.append(neighbor)
				neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False