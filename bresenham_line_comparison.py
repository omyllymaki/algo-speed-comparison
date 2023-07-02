import time

import numpy as np
from matplotlib import pyplot as plt

from bresenham_line import python_version, numba_version, cython_version


def comparison():
    start_points_int = np.loadtxt("data/start_points_int.txt").astype(int)
    end_points_int = np.loadtxt("data/end_points_int.txt").astype(int)

    max_start_points_int = np.max(start_points_int, axis=0)
    max_end_points_int = np.max(end_points_int, axis=0)

    x_max = max(max_start_points_int[0], max_end_points_int[0]) + 1
    y_max = max(max_start_points_int[1], max_end_points_int[1]) + 1

    grid = np.zeros((x_max, y_max), dtype=np.int32)

    print(f"grid size: {grid.shape}")

    methods = {
        "python": python_version.fill_grid_with_bresenham_lines,
        "numba": numba_version.fill_grid_with_bresenham_lines,
        "cython": cython_version.fill_grid_with_bresenham_lines
    }

    # Run numba version once before analysis to compile
    t = grid.copy()
    numba_version.fill_grid_with_bresenham_lines(start_points_int[:2], end_points_int[:2], t)

    for method_name, method in methods.items():

        grid1 = grid.copy()
        grid2 = grid.copy()

        t1 = time.time()
        method(start_points_int, end_points_int, grid1)
        t2 = time.time()
        n_lines_per_second = int(start_points_int.shape[0] / (t2 - t1))
        print(f"Version {method_name}: {n_lines_per_second} lines per second")

        method(start_points_int[:10], end_points_int[:10], grid2)

        plt.figure()
        plt.imshow(grid2.T > 0, cmap="gray", aspect="auto")
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
