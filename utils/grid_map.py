# Code for generating and manipulating grid maps
import numpy as np


def create_empty_grid(width: int, height: int):
    """
    Return a 2D numpy array filled with zeros (free space).
    """
    return np.zeros((height, width))


def add_wall(grid, var_range: range, fixed: int, axis='horizontal'):
    """
    Set grid[x, y(fixed)] = 1 for x in x_range, a horizontal wall.
    Or set grid[x(fixed), y] = 1 for y in y_range, a vertical wall.
    Mutates the input grid.
    """
    if axis == 'horizontal':
        for x in var_range:
            grid[x, fixed] = 1
    elif axis == 'vertical':
        for y in var_range:
            grid[fixed, y] = 1


def add_random_obstacles(grid, density: float = 0.1, seed: int = None, exclude: list = None):
    """
    Randomly add obstacles to the grid with a given density (0 to 1).
    """
    if seed is not None:
        np.random.seed(seed)

    mask = np.random.rand(*grid.shape) < density
    if exclude:
        # let x, y = start, goal!! add_random_obstacles(grid, density=0.8, exclude=[start, goal])
        for (x, y) in exclude:
            mask[y, x] = False

    grid[mask] = 1
