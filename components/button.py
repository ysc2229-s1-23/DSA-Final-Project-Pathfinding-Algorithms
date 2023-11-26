import pygame
from components.constants import *

"-----DISPLAY SETTINGS ------"

pygame.init()

BUTTON_WIDTH, BUTTON_HEIGHT = 175, 50
BUTTON_MARGIN = 80

button_font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 64)

#Dictionary to Hold Button Positions
buttons = {
    "Dijkstra": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60, BUTTON_WIDTH, BUTTON_HEIGHT),
    "A*": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT),
    "BFS": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT),
    "Fringe": pygame.Rect(BUTTON_MARGIN, BUTTON_MARGIN + 60 + 3 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT)
}

INSTRUCTION_BOX_WIDTH = 250
INSTRUCTION_BOX_HEIGHT = HEIGHT - 3 * BUTTON_MARGIN - 20
INSTRUCTION_BOX_X = WIDTH - INSTRUCTION_BOX_WIDTH - BUTTON_MARGIN
INSTRUCTION_BOX_Y = BUTTON_MARGIN + 60

instruction_box = pygame.Rect(INSTRUCTION_BOX_X, INSTRUCTION_BOX_Y, INSTRUCTION_BOX_WIDTH, INSTRUCTION_BOX_HEIGHT)
instruction_font = pygame.font.Font(None, 24)
instruction_text = (
    "\n"
	"--------USER GUIDE--------\n"
	"\n"
	"Choose an algorithm\n"
	"\n"
    "1st click is start node\n"
	"\n"
    "2nd click is end node\n"
	"\n"
    "Then create barriers (black)\n"
	"\n"
	"Right click to deselect nodes\n"
	"\n"
	"Press spacebar to find path\n"
	"\n"
	"Press 'R' to keep same nodes\n"
	"\n"
	"Press 'C' to clear everything\n"
	"\n"
	"Have fun! :)"
)

#helper function to create instruction box at the start of the visualizer, used in handle_button_events function
def draw_instruction_box(win):

    pygame.draw.rect(win, WHITE, instruction_box, border_radius=20)
    
    lines = instruction_text.split('\n')
    y_offset = instruction_box.y + 15  # Adjust the starting y-coordinate for better alignment
    for line in lines:
        line_text = instruction_font.render(line, True, BLACK)
        line_rect = line_text.get_rect(midleft=(instruction_box.x + 20, y_offset))
        win.blit(line_text, line_rect.topleft)
        y_offset += line_rect.height + 5 


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

		title_text = title_font.render("Choose Pathfinding Algorithm", True, BLACK)
        
		title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        
		win.blit(title_text, title_rect.topleft)

	
		for button_name, button_rect in buttons.items():
			pygame.draw.rect(win, color, button_rect, border_radius=20)
			button_text = button_font.render(button_name, True, WHITE)
			text_rect = button_text.get_rect(center=button_rect.center)
			win.blit(button_text, text_rect.topleft)

		draw_instruction_box(win)

		pygame.display.flip()