import dill as pickle

#SAMPLE GRIDS (contains dictionary of particular grid configuration.)
# grid with no shortest path:
with open("test_grids/nopath", 'rb') as file:
    db = pickle.load(file)
    no_grid = db["grid"]
    no_start = db["start"]
    no_end = db["end"]

# grid with one shortest path:
with open("test_grids/onepath", 'rb') as file:
    db = pickle.load(file)
    one_grid = db["grid"]
    one_start = db["start"]
    one_end = db["end"]

# simple test grid:
with open("test_grids/simplecase", 'rb') as file:
    db = pickle.load(file)
    simple_grid = db["grid"]
    simple_start = db["start"]
    simple_end = db["end"]

# complex test grid:
with open("test_grids/complexcase", 'rb') as file:
    db = pickle.load(file)
    complex_grid = db["grid"]
    complex_start = db["start"]
    complex_end = db["end"]

# complex2 test grid:
with open("test_grids/complex2case", 'rb') as file:
    db = pickle.load(file)
    complex2_grid = db["grid"]
    complex2_start = db["start"]
    complex2_end = db["end"]
