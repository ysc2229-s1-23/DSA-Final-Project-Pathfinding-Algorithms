import pytest
from components.constants import WIDTH
from algorithms.a_star import h, a_star_algo
from components.spot import Spot
from test_grids.hold_val import no_end, no_grid, no_start, one_end, one_grid, one_start, simple_end, simple_grid, simple_start, simple_end, complex2_end, complex2_grid, complex2_start, complex_end, complex_grid, complex_start


@pytest.mark.parametrize("p1, p2, manhattan_dist", [
    (Spot(5, 8, WIDTH, 50), Spot(4, 3, WIDTH, 50), 6),
    (Spot(15, 100, WIDTH, 50),Spot(700, 700, WIDTH, 50), 1285),
    (Spot(700,700, WIDTH, 50), Spot(700, 700, WIDTH, 50), 0)
])

def test_h_function(p1, p2, manhattan_dist):
    result = h(p1, p2)
    assert result == manhattan_dist

@pytest.mark.parametrize("grid, start, end, path_found, nodes_traversed, path_len", [
    #edge case
    (no_grid, no_start, no_end, False, 0, None),

    #one shortest path
    (one_grid, one_start, one_end, True, 42, 16),

    #other examples
    (simple_grid, simple_start, simple_end, True, 75, 21),
    (complex_grid, complex_start, complex_end, True, 159, 41),
    (complex2_grid, complex2_start, complex2_end, True, 82, 18)
])

def test_a_star_function(grid, start, end, path_found, nodes_traversed, path_len):
    path, count, length = a_star_algo(None, grid, start, end, True)
    assert (path, count, length) == (path_found, nodes_traversed, path_len)

