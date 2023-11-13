import pygame
from queue import PriorityQueue
from components.grid import *
from components.spot import *
from algorithms.a_star import a_star_algo

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))

def main(win, width, rows):
	grid = make_grid(rows, width)

	start = None
	end = None

	run = True #flag for whether an algorithm is running

	# TODO: This is the server
	## 1. Add a button to select the algorithm
	

	while run:
		draw(win, grid, rows, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			## 2. You must be able to select the start and end nodes
			## 3. You must be able to add barriers
			if pygame.mouse.get_pressed()[0]: # LEFT click
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			## 4. You must be able to reset the grid
			elif pygame.mouse.get_pressed()[2]: # RIGHT click
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					### algorithm defined by user choice - TO CHANGE
					a_star_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					## 6. The visualizer must stop once the start and end nodes find each other.
					## 7. A path must be drawn from the start node to the end node once the visualizer has finished.
					# these are both handled by code for each algorithm

				## 5. You must be able to run the visualizer again after it has finished
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(rows, width)

	pygame.quit()

	pass

main(WIN, WIDTH, 50) # eventually let init handle this? but for now run from here