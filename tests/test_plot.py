import numpy as np
import matplotlib.pyplot as plt
from planner.astar import astar
from planner.bspline import bspline
from utils.grid_map import create_empty_grid, add_wall, add_random_obstacles
from visualization.plot import plot_all


def test_static_plot():
    width, height = 30, 30
    grid = create_empty_grid(width, height)
    # add_wall(grid, range(5, 25), fixed=15, axis='horizontal')

    start = (0, 0)
    goal = (29, 29)

    add_random_obstacles(grid, density=0.4, seed=42,
                         exclude=[start, goal])

    path = astar(grid, start, goal)
    if not path:
        print("No path found.")
        return

    smooth_path = bspline(path)

    plot_all(grid, path, smooth_path, start, goal)


if __name__ == "__main__":
    test_static_plot()
