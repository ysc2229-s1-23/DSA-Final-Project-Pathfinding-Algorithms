import pygame
from components.constants import *

# TODO:
    ## Implement the class of one node in the grid
    ## Remember to add the necessary attributes and methods
    ## Hint: You must be able to update the neighbors of a node

class Spot:
    """
    A class used to represent a node in the grid.

    ...
    Attributes
    ----------
    row : int
        The row index of the node in the grid.
    
    col : int
        The column index of the node in the grid.

    width : int
        The width of the node.

    x : int
        The x-coordinate of the node in the window.

    y : int
        The y-coordinate of the node in the window.

    color : tuple
        The RGB tuple representing the color of the node.

    neighbors : list
        A list of neighboring nodes.

    total_rows : int
        The total number of rows in the grid.
    
    Methods
    -------
    get_pos(self)
        Returns the row and column of the node.

    is_closed(self)
        Checks if the node is closed. 

    is_open(self)
        Checks if the node is open.

    is_barrier(self)
        Checks if the node is a barrier.

    is_start(self)
        Checks if the node is the start node.

    is_end(self)
        Checks if the node is the end node.

    is_path(self)
        Checks if the node is part of the path.

    reset(self)
        Resets the color of node back to WHITE.
    
    make_start(self)
        Changes the color of node to ORANGE.

    make_closed(self)
        Changes the color of the node to RED.

    make_open(self)
        Changes the color of the node to GREEN.

    make_barrier(self)
        Changes the color of the node to BLACK.

    make_end(self)
        Changes the color of the node to TURQUOISE.

    make_path(self)
        Changes the color of the node to PURPLE.

    draw(self, win)
        Draws the node on the window
    
    update_neighbors(self, grid)
        Stores the valid neighbours of the node.

    __lt__(self, other)
        Less than comparison method.


    """
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """Returns the row and column of the node."""
        return self.row, self.col
    
    def is_closed(self):
        """
        Checks if the node is closed.

        Returns
        -------
        bool
            True if the node is closed, False otherwise.
        """
        return self.color == RED
    
    def is_open(self):
        """
        Checks if the node is open.

        Returns
        -------
        bool
            True if the node is open, False otherwise.
        """
        return self.color == GREEN
    
    def is_barrier(self):
        """
        Checks if the node is a barrier.

        Returns
        -------
        bool
            True if the node is a barrier, False otherwise.
        """
        return self.color == BLACK
    
    def is_start(self):
        """
        Checks if the node is the start node.

        Returns
        -------
        bool
            True if the node is the start node, False otherwise.
        """
        return self.color == ORANGE
    
    def is_end(self):
        """
        Checks if the node is the end node.

        Returns
        -------
        bool
            True if the node is the end node, False otherwise.
        """
        return self.color == TURQUOISE
    
    def is_path(self):
        """
        Checks if the node is part of the path.

        Returns:
        - (bool): True if the node is part of the path, False otherwise.
        """
        return self.color == PURPLE
    
    def reset(self):
        """Resets the color of the node back to WHITE."""
        self.color = WHITE
    
    def make_start(self):
        """Changes the color of the node to ORANGE."""
        self.color = ORANGE

    def make_closed(self):
        """Changes the color of the node to RED."""
        self.color = RED

    def make_open(self):
        """Changes the color of the node to GREEN."""
        self.color = GREEN

    def make_barrier(self):
        """Changes the color of the node to BLACK."""
        self.color = BLACK

    def make_end(self):
        """Changes the color of the node to TURQUOISE."""
        self.color = TURQUOISE

    def make_path(self):
        """Changes the color of the node to PURPLE."""
        self.color = PURPLE

    def draw(self, win):
        """
        Draws the node (including its color) on the window.

        Args:
        - win (pygame.Surface): The window surface on which to draw the node.
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        """
        Stores the valid neighbors of the node.

        Parameters
        ----------
        grid : list
            The grid containing the nodes.
        """
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    # def __lt__(self, other): #need this?
    #     """
    #     Less than comparison method, not currently used.

    #     Parameters
    #     ----------
    #     other : Spot
    #         The other Spot object to compare.

    #     Returns
    #     -------
    #     bool
    #         False, as the method is not currently used for comparison.
    #     """
    #     return False
