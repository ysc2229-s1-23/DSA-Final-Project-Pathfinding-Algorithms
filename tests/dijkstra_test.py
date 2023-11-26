import pytest
from components.constants import WIDTH
from algorithms.dijkstra import dijkstra_algo
from components.spot import Spot
import dill as pickle 
from test_grids.hold_val import no_end, no_grid, no_start, one_end, one_grid, one_start, simple_end, simple_grid, simple_start, simple_end, complex2_end, complex2_grid, complex2_start, complex_end, complex_grid, complex_start

@pytest.mark.parametrize("grid, start, end, path_found, nodes_traversed, path_len", [
    #Edge Case
     (no_grid, no_start, no_end, False, 0, None),

    #One Shortest Path
    (one_grid, one_start, one_end, True, 49, 16),

    #Other Test Cases
    (simple_grid, simple_start, simple_end, True, 87, 21),
    (complex_grid, complex_start, complex_end, True, 349, 41),
    (complex2_grid, complex2_start, complex2_end, True, 629, 18),
   
])

def test_dijkstra_function(grid, start, end, path_found, nodes_traversed, path_len):
    path, count, length = dijkstra_algo(None, grid, start, end, True)
    assert (path, count, length) == (path_found, nodes_traversed, path_len)