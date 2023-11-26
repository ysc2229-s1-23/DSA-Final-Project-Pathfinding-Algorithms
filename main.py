import pygame
from timeit import default_timer as timer
# import sys
from queue import PriorityQueue
from components.grid import *
from components.spot import *
from components.button import *
from components.constants import *
from algorithms.a_star import a_star_algo
from algorithms.fringe import fringe_algo
from algorithms.ripcode import ida_star_algo
from algorithms.bfs import bfs_algo
from algorithms.dijkstra import dijkstra_algo

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH))

def main(win, width, rows):
	"""
	Main function to run the simulations.

	Args:
	- win (pygame.Surface) : Initialized display screen.
	- width (int) : Width of the grid.
	- rows (int) : Number of grid rows.

	Returns:
	- Runs the simulation.
	"""
	grid = make_grid(rows, width)

	start = None
	end = None

	run = True # flag for whether an algorithm is running
	algorithm = None # variable for user-selected algorithm
	selected = False # flag for whether an algorithm has been selected
	
	
	stat_font = pygame.font.Font(None, 20)
	present_stat = stat_font.render("", True, BLACK) 
	# buffer = pygame.display.set_mode((WIDTH, WIDTH))
	

	update_stats = True
	while run:
		path_found = None #somehow this is impt for the thing to not pop off....
		
		if start == None: # first run or cleared
			win.fill(WHITE) #nedit: is this redundant bc win.fill(WHITE) also in draw function
			draw(win, grid, rows, width)
			# buffer.fill(WHITE)
			# draw(buffer, grid, rows, width)
		## 1. Add a button to select the algorithm
		if selected == False:
			algorithm = handle_button_events(win, BUTTON_COL)
			# algorithm = handle_button_events(buffer, BUTTON_COL) #nedit
			selected = True

		# once algorithm is selected, draw the grid
		draw(win, grid, rows, width) #nedit: shld this be indented if it's draw grid when selected algo
		# draw(buffer, grid, rows, width) #nedit

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

			## 4. You must be able to reset the grid #nedit: maybe can add button to reset everything?  

			# #nedit: this is retracting clicks but not necessarily resetting whole grid?
			elif pygame.mouse.get_pressed()[2]: # RIGHT click
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				spot.reset() #reset method in Spot class changing node back to white
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
					if algorithm == "A*" or algorithm == None:
						start_time = timer()
						path_found, count, path_len = a_star_algo(lambda: draw(win, grid, rows, width), grid, start, end)
						end_time = timer()
						traversal_time = end_time - start_time

					elif algorithm == "Dijkstra":
						start_time = timer()
						path_found, count, path_len = dijkstra_algo(lambda: draw(win, grid, rows, width), grid, start, end)
						end_time = timer()
						traversal_time = end_time - start_time

					elif algorithm == "BFS":
						start_time = timer()
						path_found, count, path_len = bfs_algo(lambda: draw(win, grid, rows, width), grid, start, end)
						end_time = timer()
						traversal_time = end_time - start_time

					elif algorithm == "Fringe":
						start_time = timer()
						path_found, count, path_len = fringe_algo(lambda: draw(win, grid, rows, width), grid, start, end)
						end_time = timer()
						traversal_time = end_time - start_time

					elif algorithm == "IDA*":
						start_time = timer()
						path_found, count, path_len = ida_star_algo(lambda: draw(win, grid, rows, width), grid, start, end)
						end_time = timer()
						traversal_time = end_time - start_time

					# stat_font = pygame.font.Font(None, 20)
					if path_found == None:
						continue
					else:
						if path_found == True:
								stats = f"Path found. Length of Path : {path_len}, Traversal Time : {traversal_time}, Nodes Traversed : {count}"
						elif path_found == False:
							stats = "Path not found."

						present_stat = stat_font.render(stats, True, BLACK)
					## 6. The visualizer must stop once the start and end nodes find each other.
					## 7. A path must be drawn from the start node to the end node once the visualizer has finished.
					# these are both handled by code for each algorithm

				## clear the previously found path, while retaining barriers
				elif event.key == pygame.K_r: # r for 'reset'
					# start_spot = start
					# end_spot = end
					path_found = None
					# grid = make_grid(rows, width)
					# start_spot.make_start()
					# end_spot.make_end()

					for row in grid:
						for spot in row:
							if spot.is_closed() or spot.is_open() or spot.is_path():
								spot.reset()
					selected = False


				## 5. You must be able to run the visualizer again after it has finished
				elif event.key == pygame.K_c: # c for 'clear'
					start = None
					end = None
					path_found = None
					grid = make_grid(rows, width)
					selected = False # ensures a different algorithm can be selected
		
		place = present_stat.get_rect(center=(WIDTH // 2, 50))
		# buffer.blit(present_stat, place.topleft)
		WIN.blit(present_stat, place.topleft)
		# WIN.blit(buffer, (0, 0))
		pygame.display.update()

	pygame.quit()

main(WIN, WIDTH, 50)