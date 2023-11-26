import pytest
from components.constants import WIDTH
from algorithms.fringe import fringe_algo
from components.spot import Spot
import dill as pickle 

#SAMPLE GRIDS (contains dictionary of particular grid configuration.)
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

@pytest.mark.parametrize("grid, start, end, path_found, nodes_traversed, path_len", [
    (no_grid, no_start, no_end, False, 0, None)#,
    # (one_grid, one_start, one_end, True, 42, 16),
])

def test_fringe_function(grid, start, end, path_found, nodes_traversed, path_len):
    path, count, length = fringe_algo(None, grid, start, end, True)
    assert (path, count, length) == (path_found, nodes_traversed, path_len)

