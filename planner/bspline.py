# B-spline optimization functions will go here
from scipy.interpolate import make_interp_spline
import numpy as np


def bspline(path, num_points=100):
    """
    Given a list of (x, y) path points, return a smoothed B-spline curve
    """
    path = np.array(path)
    x, y = path[:, 0], path[:, 1]  # obtaining x, y jagged path solved from a*
    t = np.linspace(0, 1, len(path))  # parametrisation into x(t), y(t)
    spl_x = make_interp_spline(t, x, k=3)  # k = cubic
    spl_y = make_interp_spline(t, y, k=3)  # and hence len(path) MUST > k (=3)
    # num_points is points to sample
    num_points = 8 * len(path)
    t_new = np.linspace(0, 1, num_points)
    x_smooth = spl_x(t_new)  # smooth points of (x1, x2...)
    y_smooth = spl_y(t_new)

    return np.column_stack((x_smooth, y_smooth))
