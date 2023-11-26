import pytest
from components.constants import WIDTH
from algorithms.bfs import bfs_algo
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
    (one_grid, one_start, one_end, True, 49, 16),
    (simple_grid, simple_start, simple_end, True, 87, 21),
    (complex_grid, complex_start, complex_end, True, 349, 41),
    (complex2_grid, complex2_start, complex2_end, True, 629, 18)
])

def test_bfs_function(grid, start, end, path_found, nodes_traversed, path_len):
    path, count, length = bfs_algo(None, grid, start, end, True)
    assert (path, count, length) == (path_found, nodes_traversed, path_len)

# import networkx as nx
# import pytest
# # from your_module import dijkstra_algorithm

# def test_dijkstra_comparison():
#     # Create a graph (replace this with your graph creation logic)
#     graph = nx.Graph()
#     graph.add_edge(0, 1, weight=2)
#     graph.add_edge(1, 2, weight=1)
#     graph.add_edge(2, 3, weight=3)

#     # Run Dijkstra's algorithm from your module
#     your_result = dijkstra_algorithm(graph, source=0, target=3)

#     # Run Dijkstra's algorithm from NetworkX
#     nx_result = nx.shortest_path(graph, source=0, target=3, weight='weight')

#     # Compare results
#     assert your_result == nx_result
