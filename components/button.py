import pygame
from components.constants import *

pygame.init()

BUTTON_WIDTH, BUTTON_HEIGHT = 175, 50
BUTTON_MARGIN = 40

button_font = pygame.font.Font(None, 36)

buttons = {
	"Dijkstra": pygame.Rect(BUTTON_MARGIN, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
	"A*": pygame.Rect(2 * BUTTON_MARGIN + BUTTON_WIDTH, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
	"Fringe": pygame.Rect(3 * BUTTON_MARGIN + 2 * BUTTON_WIDTH, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
}

def handle_button_events(win, color):
	"""
	Function to display algorithm options on screen and return name of algorithm chosen

	Args:
	- win : initialization of display screen (pygame.display.set_mode((WIDTH, WIDTH)))
	- color (tuple): The color of the button box 

	Returns:
	- Displays buttons for each algorithm for user to select.
	- button_name (str) : Name of algorithm selected to run. 
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

		for button_name, button_rect in buttons.items():
			pygame.draw.rect(win, color, button_rect)
			button_text = button_font.render(button_name, True, BLACK)
			win.blit(button_text, (button_rect.x+45, button_rect.y+15))
#nedit: button_rect.x used to be  + 20 not + 45 -- but perhaps find a better way to center text?
		pygame.display.flip()