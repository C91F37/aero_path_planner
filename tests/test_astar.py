# Unit tests for A* implementation
import numpy as np
from planner.astar import astar


def print_grid(grid, path):
    grid_copy = grid.copy()
    for x, y in path:
        if grid_copy[x, y] == 0:
            grid_copy[x, y] = 2  # mark path
    for row in grid_copy:
        print(''.join(['#' if c == 1 else '.' if c == 0 else '*' for c in row]))
        # '#' is obstacle, '.' is node, and * is path


def test_astar():
    grid = np.zeros((10, 10), dtype=int)
    # Add some obstacles
    grid[1:8, 3] = 1
    grid[2, 3:7] = 1
    start = (0, 0)
    goal = (7, 8)

    path = astar(grid, start, goal)

    if path:
        print("Félicitations !! Path found:")
        print(path)
        print_grid(grid, path)
    else:
        print("C'est dommage... No path found.")


if __name__ == "__main__":
    test_astar()
