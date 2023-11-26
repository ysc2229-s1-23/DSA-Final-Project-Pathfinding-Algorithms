import pygame
from timeit import default_timer as timer
from queue import PriorityQueue
from components.grid import *
from components.spot import *
from components.button import *
from components.constants import *
from algorithms.a_star import a_star_algo
from algorithms.fringe import fringe_algo
from ripcode import ida_star_algo
from algorithms.bfs import bfs_algo
from algorithms.dijkstra import dijkstra_algo

'----MAIN FUNCTION TO RUN VISUALIZER------'

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
	display = False #flag to avoid flickering
	path_found = None #impt for the pathfinding statistics to not pop off.
	stat_font = pygame.font.Font(None, 20)
	present_stat = stat_font.render("", True, BLACK) 

	while run:
		
		if not display:
		# if start == None: # first run or cleared
			# win.fill(WHITE) 
			draw(win, grid, rows, width)

		## Button to select the algorithm
		if selected == False:
			algorithm = handle_button_events(win, BUTTON_COL)
			selected = True

		# once algorithm is selected, draw the grid
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
				spot.reset() #reset method in Spot class changing node back to white
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							if spot.is_closed() or spot.is_open() or spot.is_path():
								spot.reset()

					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					start_time = timer()

					### algorithm defined by user choice 
					if algorithm == "A*" or algorithm == None:
						path_found, count, path_len = a_star_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					elif algorithm == "Dijkstra":
						path_found, count, path_len = dijkstra_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					elif algorithm == "BFS":
						path_found, count, path_len = bfs_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					elif algorithm == "Fringe":						
						path_found, count, path_len = fringe_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					
					end_time = timer()
					traversal_time = end_time - start_time
					display = True

					if path_found == None:
						continue
					else:
						display = True
						if path_found == True:
							stats = f"Path found. Length of Path : {path_len}, Traversal Time : {traversal_time}, Nodes Traversed : {count}"
						elif path_found == False:
							stats = "Path not found."

						present_stat = stat_font.render(stats, True, BLACK)
					
					## 6. The visualizer must stop once the start and end nodes find each other.
					## 7. A path must be drawn from the start node to the end node once the visualizer has finished.
					# these are both handled by code for each algorithm

				## clear the previously found path, while retaining barriers
				if event.key == pygame.K_r: # r for 'reset'
					display = False
					path_found = None
			
					for row in grid:
						for spot in row:
							if spot.is_closed() or spot.is_open() or spot.is_path():
								spot.reset()
					selected = False

				## 5. You must be able to run the visualizer again after it has finished
				if event.key == pygame.K_c: # c for 'clear'
					display = False
					start = None
					end = None
					path_found = None
					grid = make_grid(rows, width)
					selected = False # ensures a different algorithm can be selected
		
	
		place = present_stat.get_rect(center=(WIDTH // 2, 50))
		WIN.blit(present_stat, place.topleft)
		pygame.display.update()

	pygame.quit()

main(WIN, WIDTH, 50)