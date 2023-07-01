import time

import numpy as np
from matplotlib import pyplot as plt

from bresenham_line import python_version, numba_version, cython_version


def prepare_data(start_points, end_points, cell_size, min_xy=None, max_xy=None):
    if (min_xy is None) or (max_xy is None):
        all_points = np.vstack((start_points, end_points))
        if min_xy is None:
            min_xy = np.min(all_points, axis=0)
        if max_xy is None:
            max_xy = np.max(all_points, axis=0)

    start_points_int = np.round((start_points - min_xy) / cell_size).astype(np.int32)
    end_points_int = np.round((end_points - min_xy) / cell_size).astype(np.int32)

    n_rows = np.ceil((max_xy[0] - min_xy[0]) / cell_size).astype(np.int32) + 1
    n_cols = np.ceil((max_xy[1] - min_xy[1]) / cell_size).astype(np.int32) + 1
    grid = np.zeros((n_rows, n_cols), dtype=np.int32)

    return start_points_int, end_points_int, grid


def comparison():
    voxel_size = 1.5
    n_lines = 20000

    start_points = np.random.uniform(-100, 100, (n_lines, 2))
    end_points = np.random.uniform(-100, 100, (n_lines, 2))

    np.savetxt("start_points.txt", start_points)
    np.savetxt("end_points.txt", end_points)

    all_points = np.vstack((start_points, end_points))
    min_xy = np.min(all_points, axis=0)
    max_xy = np.max(all_points, axis=0)

    start_points_int, end_points_int, grid = prepare_data(start_points,
                                                          end_points,
                                                          voxel_size,
                                                          min_xy=min_xy,
                                                          max_xy=max_xy)

    np.savetxt("start_points_int.txt", start_points_int)
    np.savetxt("end_points_int.txt", end_points_int)

    print(f"Grid size: {grid.shape}")

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
        n_lines_per_second = int(n_lines / (t2 - t1))
        print(f"Version {method_name}: {n_lines_per_second} lines per second")

        method(start_points_int[:10], end_points_int[:10], grid2)

        plt.figure()
        plt.imshow(grid2.T > 0, cmap="gray", aspect="auto")
        plt.gca().invert_yaxis()
        sps = (start_points[:10] - min_xy) / voxel_size
        eps = (end_points[:10] - min_xy) / voxel_size
        for (sp, ep) in zip(sps, eps):
            xs = [sp[0], ep[0]]
            ys = [sp[1], ep[1]]
            plt.plot(xs, ys, "r-")

        plt.title(method_name)

    plt.show()


if __name__ == "__main__":
    comparison()
