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



# def calculate_distance(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# import pytest
# from your_code import calculate_distance

# # Assume your_code.py contains the calculate_distance function

# @pytest.mark.parametrize("x1, y1, x2, y2, expected_distance", [
#     (0, 0, 3, 4, 5.0),
#     (0, 0, 1, 1, 1.414),  # Square root of 2
#     (0, 0, -3, -4, 5.0),  # Negative coordinates
#     (1, 1, 1, 1, 0.0),  # Same point, distance should be 0
# ])
# def test_distance_calculation(x1, y1, x2, y2, expected_distance):
#     result = calculate_distance(x1, y1, x2, y2)
#     assert result == expected_distance
