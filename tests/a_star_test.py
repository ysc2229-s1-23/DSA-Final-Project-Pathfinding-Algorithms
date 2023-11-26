import pytest
from components.constants import WIDTH
from algorithms.a_star import h, a_star_algo
from components.spot import Spot
import dill as pickle 


@pytest.mark.parametrize("p1, p2, manhattan_dist", [
    (Spot(5, 8, WIDTH, 50), Spot(4, 3, WIDTH, 50), 6),
    (Spot(15, 100, WIDTH, 50),Spot(700, 700, WIDTH, 50), 1285),
    (Spot(700,700, WIDTH, 50), Spot(700, 700, WIDTH, 50), 0)
])

def test_h_function(p1, p2, manhattan_dist):
    result = h(p1, p2)
    assert result == manhattan_dist

#SAMPLE GRIDS
# grid with no shortest path:
with open("nopath", 'rb') as file:
    db = pickle.load(file)
    no_grid = db["grid"]
    no_start = db["start"]
    no_end = db["end"]

# grid with one shortest path:
with open("onepath", 'rb') as file:
    db = pickle.load(file)
    one_grid = db["grid"]
    one_start = db["start"]
    one_end = db["end"]

# simple test grid:
with open("simplecase", 'rb') as file:
    db = pickle.load(file)
    simple_grid = db["grid"]
    simple_start = db["start"]
    simple_end = db["end"]


# complex test grid:
with open("complexcase", 'rb') as file:
    db = pickle.load(file)
    complex_grid = db["grid"]
    complex_start = db["start"]
    complex_end = db["end"]

# complex2 test grid:
with open("complex2case", 'rb') as file:
    db = pickle.load(file)
    complex2_grid = db["grid"]
    complex2_start = db["start"]
    complex2_end = db["end"]

@pytest.mark.parametrize("grid, start, end, path_found, nodes_traversed, path_len", [
    (no_grid, no_start, no_end, False, 0, None),
    (one_grid, one_start, one_end, True, 42, 16),
    (simple_grid, simple_start, simple_end, True, 75, 21),
    (complex_grid, complex_start, complex_end, True, 159, 41),
    (complex2_grid, complex2_start, complex2_end, True, 82, 18)
])

def test_a_star_function(grid, start, end, path_found, nodes_traversed, path_len):
    path, count, length = a_star_algo(None, grid, start, end, True)
    assert (path, count, length) == (path_found, nodes_traversed, path_len)

