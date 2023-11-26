import pytest
from components.constants import WIDTH
from algorithms.fringe import fringe_algo
from components.spot import Spot
from test_grids.hold_val import no_end, no_grid, no_start, complex_end, complex_grid, complex_start


@pytest.mark.parametrize("grid, start, end, path_found, nodes_traversed, path_len", [
    (no_grid, no_start, no_end, False, 0, None),
    (complex_grid, complex_start, complex_end, True, 627, 41) #case where fringe actually finds the shortest path.
])

def test_fringe_function(grid, start, end, path_found, nodes_traversed, path_len):
    """
    Note: for Fringe function, due to some irregularities, we mainly test whether it terminates correctly 
    and finds a path if there is a viable one.
    """
    path, count, length = fringe_algo(None, grid, start, end, True)
    assert (path, count, length) == (path_found, nodes_traversed, path_len)

