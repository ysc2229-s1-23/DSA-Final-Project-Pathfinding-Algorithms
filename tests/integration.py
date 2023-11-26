import pytest
from components.constants import WIDTH
from algorithms.a_star import h, a_star_algo
from algorithms.bfs import bfs_algo
from algorithms.dijkstra import dijkstra_algo
from components.spot import Spot
from test_grids.hold_val import no_end, no_grid, no_start, one_end, one_grid, one_start, simple_end, simple_grid, simple_start, simple_end, complex2_end, complex2_grid, complex2_start, complex_end, complex_grid, complex_start

@pytest.mark.parametrize("grid, start, end, path_found, nodes_traversed, path_len", [
    (no_grid, no_start, no_end, False, 0, None),
    (one_grid, one_start, one_end, True, 49, 16),
    (simple_grid, simple_start, simple_end, True, 87, 21),
    (complex_grid, complex_start, complex_end, True, 349, 41),
    (complex2_grid, complex2_start, complex2_end, True, 629, 18)
])

def integration_test_function(grid, start, end, path_found, nodes_traversed, path_len):

    a_star_path, a_star_count, a_star_len = a_star_algo(None, grid, start, end, True)
    bfs_path, bfs_count, bfs_len = bfs_algo(None, grid, start, end, True)
    dijkstra_path, dijkstra_count, dijkstra_len = bfs_algo(None, grid, start, end, True)

    path_found_for_all = a_star_path and bfs_path and dijkstra_path

    count_relation = (a_star_count < bfs_count and a_star_count < dijkstra_count) #case studies where A* is faster

    if a_star_len == bfs_len and bfs_len == dijkstra_len:
        same_len = True
    else:
        same_len = False

    assert (path_found_for_all, count_relation, same_len) == (path_found, nodes_traversed, path_len)
