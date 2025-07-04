# Visualization utilities using matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_grid(grid, ax=None):
    """
    Visualize grid map using imshow.
    0 = free space (white), 1 = obstacle (black).
    """
    if ax is None:
        ax = plt.gca()
    ax.imshow(grid.T, cmap='Greys')


def plot_start_goal(start, goal, ax=None):
    """
    Mark start (green dot) and goal (red dot).
    """
    if ax is None:
        ax = plt.gca()
    ax.plot(start[0], start[1], 'go', label='Start')
    ax.plot(goal[0], goal[1], 'ro', label='Goal')


def plot_path(path, color='gray', label='A* Path', ax=None):
    """
    Draw a zigzag path from list of (x, y).
    """
    if ax is None:
        ax = plt.gca()
    path_arr = np.array(path)
    ax.plot(path_arr[:, 0], path_arr[:, 1],
            'o', label="A* Path", color="gray")


def plot_bspline(smooth_path, color='blue', label='B-Spline', ax=None):
    """
    Plot a smooth path.
    """
    if ax is None:
        ax = plt.gca()
    ax.plot(smooth_path[:, 0], smooth_path[:, 1],
            '-', label="B-Spline", color="blue")


def plot_all(grid, path, smooth_path, start, goal):
    """
    Plot everything (grid, start/goal, A* path, B-spline).
    """
    fig, ax = plt.subplots()
    plot_grid(grid, ax=ax)
    plot_path(path, ax=ax)
    plot_bspline(smooth_path, ax=ax)
    plot_start_goal(start, goal, ax=ax)
    ax.set_title("Grid Map")
    ax.legend()
    ax.axis('equal')
    ax.grid(True)
    plt.show()
