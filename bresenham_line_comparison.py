import time

import numpy as np
from matplotlib import pyplot as plt

from bresenham_line import python_version, numba_version, cython_version

import sys
sys.path.append("/home/ossi/Repos/Personal/algo-speed-comparison/bresenham_line/build")
from example import rasterize_lines


def comparison():
    start_points_int = np.loadtxt("data/start_points_int.txt").astype(int)
    end_points_int = np.loadtxt("data/end_points_int.txt").astype(int)

    max_start_points_int = np.max(start_points_int, axis=0)
    max_end_points_int = np.max(end_points_int, axis=0)

    x_max = max(max_start_points_int[0], max_end_points_int[0]) + 1
    y_max = max(max_start_points_int[1], max_end_points_int[1]) + 1
    grid_dim = (x_max, y_max)

    print(f"grid size: {grid_dim}")

    methods = {
        "python": python_version.rasterize_lines,
        "numba": numba_version.rasterize_lines,
        "cython": cython_version.rasterize_lines,
        "C++ binding": rasterize_lines
    }

    # Run numba version once before analysis to compile
    numba_version.rasterize_lines(start_points_int[:2], end_points_int[:2], grid_dim)

    for method_name, method in methods.items():

        t1 = time.time()
        method(start_points_int, end_points_int, grid_dim)
        t2 = time.time()
        n_lines_per_second = int(start_points_int.shape[0] / (t2 - t1))
        print(f"Version {method_name}: {n_lines_per_second} lines per second")

        grid = method(start_points_int[:10], end_points_int[:10], grid_dim)

        plt.figure()
        plt.imshow(grid.T > 0, cmap="gray", aspect="auto")
        plt.gca().invert_yaxis()
        sps = start_points_int[:10]
        eps = end_points_int[:10]
        for (sp, ep) in zip(sps, eps):
            xs = [sp[0], ep[0]]
            ys = [sp[1], ep[1]]
            plt.plot(xs, ys, "r-")

        plt.title(method_name)

    plt.show()


if __name__ == "__main__":
    comparison()
