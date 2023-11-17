import pygame
# import sys
from queue import PriorityQueue
from components.grid import *
from components.spot import *
from algorithms.a_star import a_star_algo

pygame.init() # to move to init?

WIDTH = HEIGHT = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH))

BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
BUTTON_MARGIN = 20

button_font = pygame.font.Font(None, 36)

buttons = {
	"Dijkstra": pygame.Rect(BUTTON_MARGIN, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
	"A*": pygame.Rect(2 * BUTTON_MARGIN + BUTTON_WIDTH, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
	"BFS": pygame.Rect(3 * BUTTON_MARGIN + 2 * BUTTON_WIDTH, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
}

def handle_button_events():
	while True:
		for button_event in pygame.event.get():
			if button_event.type == pygame.QUIT:
				pygame.quit()
			elif button_event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()

				for button_name, button_rect in buttons.items():
					if button_rect.collidepoint(mouse_pos):
						return button_name

		for button_name, button_rect in buttons.items():
			pygame.draw.rect(WIN, GREY, button_rect)
			button_text = button_font.render(button_name, True, BLACK)
			WIN.blit(button_text, button_rect.center)

		pygame.display.flip()

def main(win, width, rows):
	grid = make_grid(rows, width)

	start = None
	end = None

	run = True # flag for whether an algorithm is running
	algorithm = None # variable for user-selected algorithm
	selected = False # flag for whether an algorithm has been selected

	while run:
		win.fill(WHITE)

		## 1. Add a button to select the algorithm
		if selected == False:
			algorithm = handle_button_events()
			selected = True
	
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
					if algorithm == "A*" or algorithm == None:
						a_star_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					# elif selected_algorithm == "Dijkstra":
					# 	dijkstra_algo(lambda: draw(win, grid, rows, width), grid, start, end)
					# elif selected_algorithm == "BFS":
					# 	bfs_algo(lambda: draw(win, grid, rows, width), grid, start, end)

					## 6. The visualizer must stop once the start and end nodes find each other.
					## 7. A path must be drawn from the start node to the end node once the visualizer has finished.
					# these are both handled by code for each algorithm

				### TODO: event to clear the previously found path, while retaining barriers
				### does this mean algo selection buttons need to be visible below grid as well? 

				## 5. You must be able to run the visualizer again after it has finished
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(rows, width)
					selected = False # ensures a different algorithm can be selected

	pygame.quit()

main(WIN, WIDTH, 50) # eventually let init handle this? but for now run from here