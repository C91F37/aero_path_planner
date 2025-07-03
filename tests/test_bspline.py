# Unit tests for B-spline implementation
import numpy as np
import matplotlib.pyplot as plt
from planner.astar import astar
from planner.bspline import bspline


def test_bspline():
    grid = np.zeros((20, 20), dtype=int)
    # Add a vertical wall with gap
    grid[5:18, 10] = 1
    grid[11, 10] = 0  # gap

    start = (2, 2)
    goal = (17, 17)

    path = astar(grid, start, goal)
    if not path:
        print("A* failed to find a path.")
        return

    smooth_path = bspline(path, num_points=200)

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.imshow(grid.T, origin='lower', cmap='Greys', alpha=0.3)

    # Original A* path
    path_arr = np.array(path)
    plt.plot(path_arr[:, 0], path_arr[:, 1],
             'o-', label="A* Path", color="gray")

    # Smoothed B-spline path
    plt.plot(smooth_path[:, 0], smooth_path[:, 1],
             '-', label="B-Spline", color="blue")

    plt.legend()
    plt.title("A* vs B-Spline Smoothed Path")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    test_bspline()
