import numpy as np


def prepare_data(start_points, end_points, cell_size, min_xy=None):
    if min_xy is None:
        all_points = np.vstack((start_points, end_points))
        min_xy = np.min(all_points, axis=0)

    start_points_int = np.round((start_points - min_xy) / cell_size).astype(int)
    end_points_int = np.round((end_points - min_xy) / cell_size).astype(int)

    return start_points_int, end_points_int


def generate_data():
    voxel_size = 1.5
    n_lines = 50000

    start_points = np.random.uniform(-100, 100, (n_lines, 2))
    end_points = np.random.uniform(-100, 100, (n_lines, 2))

    all_points = np.vstack((start_points, end_points))
    min_xy = np.min(all_points, axis=0)

    start_points_int, end_points_int = prepare_data(start_points,
                                                    end_points,
                                                    voxel_size,
                                                    min_xy=min_xy)

    np.savetxt("data/start_points.txt", start_points)
    np.savetxt("data/end_points.txt", end_points)

    np.savetxt("data/start_points_int.txt", start_points_int)
    np.savetxt("data/end_points_int.txt", end_points_int)


if __name__ == "__main__":
    generate_data()
