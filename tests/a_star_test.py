import pytest
from components.constants import WIDTH
from algorithms.a_star import h, a_star_algo
from components.spot import Spot

@pytest.mark.parametrize("p1, p2, manhattan_dist", [
    (Spot(5, 8, WIDTH, 50), Spot(4, 3, WIDTH, 50), 6),
    (Spot(15, 100, WIDTH, 50),Spot(700, 700, WIDTH, 50), 1285),
    (Spot(700,700, WIDTH, 50), Spot(700, 700, WIDTH, 50), 0)
])


def test_h_function(p1, p2, manhattan_dist):
    result = h(p1, p2)
    assert result == manhattan_dist

# @pytest.mark.parametrize(
# a_star_algo(draw, grid: list, start: Spot, end: Spot):
# a_star_algo(lambda: draw(win, grid, rows, width), grid, start, end)
# # GRID = 
# @pytest.mark.parametrize("start, end, draw, expected_result", [
#     ((0, 0), Spot(4, 4), True),  # Example case where there's a path
#     ((0, 0), (0, 0), True),  # Case where start and end are the same (should also return True)
#     # Add more test cases as needed
# ])

# def test_a_star_basic(start, end, draw, expected_result):
#     # Create a small grid for testing
#     grid = [[Spot(row, col) for col in range(5)] for row in range(5)]

#     # Set start and end positions
#     start = grid[start_coords[0]][start_coords[1]]
#     end = grid[end_coords[0]][end_coords[1]]

#     # Run the A* algorithm
#     result = a_star_algo(lambda: draw(WIN, GRID, 50, WIDTH), GRID, start, end)

#     # Assert the result
#     assert result == expected_result

