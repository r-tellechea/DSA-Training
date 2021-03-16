from paths_in_a_grid import Grid

grid = Grid([
    [3, 7, 9, 2, 7],
    [9, 8, 3, 5, 5],
    [1, 7, 9, 8, 5],
    [3, 8, 6, 4, 10],
    [6, 3, 9, 7, 8],
])

print(67 == grid.lower_path_sum())
