import numpy as np
from skimage.draw import line


def rasterize_lines(start_points, end_points, grid_dim):
    grid = np.zeros(grid_dim, dtype=np.uint)
    for i in range(start_points.shape[0]):
        sp = start_points[i]
        ep = end_points[i]
        rr, cc = line(sp[0], sp[1], ep[0], ep[1])
        grid[rr, cc] += 1
    return grid
