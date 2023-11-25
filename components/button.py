import pygame
from components.constants import *

pygame.init()

BUTTON_WIDTH, BUTTON_HEIGHT = 175, 50
BUTTON_MARGIN = 60

button_font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 64)

# buttons = {
#     "Dijkstra": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
#     "A*": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
#     "BFS": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
#     "Fringe": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 3 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
#     "IDA": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 4 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
# }
buttons = {
    "Dijkstra": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60, BUTTON_WIDTH, BUTTON_HEIGHT),
    "A*": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
    "BFS": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
    "Fringe": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + 3 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
    "IDA": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + 4 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
}

def handle_button_events(win, color):
	"""
	Function to display algorithm options on screen and return name of algorithm chosen.

	Args:
	- win (pygame.Surface): The display screen used.
	- color (tuple): The RGB color tuple for the button box. 

	Returns:
	- button_name (str) : Name of algorithm selected to run. 

	Displays buttons for each algorithm for user to select.
	"""
	while True:
		for button_event in pygame.event.get():
			if button_event.type == pygame.QUIT:
				pygame.quit()
			elif button_event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				for button_name, button_rect in buttons.items():
					if button_rect.collidepoint(mouse_pos):
						return button_name
		
		# win.fill(BLACK) #clear screen before redrawing button???

		title_text = title_font.render("Choose Pathfinding Algorithm", True, BLACK)
        
		title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        
		win.blit(title_text, title_rect.topleft)

	
		for button_name, button_rect in buttons.items():
			pygame.draw.rect(win, color, button_rect, border_radius=20)
			button_text = button_font.render(button_name, True, WHITE)
			text_rect = button_text.get_rect(center=button_rect.center)
			win.blit(button_text, text_rect.topleft)
			
		pygame.display.flip()