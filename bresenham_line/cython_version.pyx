import numpy as np
cimport numpy as np
cimport cython


@cython.boundscheck(False)
cdef int fill_grid_with_bresenham_line(unsigned x0, unsigned y0,
                                       unsigned x1, unsigned y1,
                                       np.ndarray[np.int32_t, ndim=2] grid):

    cdef int e2, sx, sy, error
    cdef int dx, dy

    if x1 > x0:
        dx = x1 - x0
    else:
        dx = x0 - x1
    
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    
    if y1 > y0:
        dy = y0 - y1
    else:
        dy = y1 - y0
    
    if y0 < y1:
        sy = 1
    else:
        sy = -1

    error = dx + dy

    while True:
        grid[x0, y0] += 1
        if (x0 == x1) and (y0 == y1):
            break
        e2 = 2 * error
        if e2 >= dy:
            if x0 == x1:
                break
            error = error + dy
            x0 = x0 + sx
        if e2 <= dx:
            if y0 == y1:
                break
            error = error + dx
            y0 = y0 + sy

    return 0



def fill_grid_with_bresenham_lines(np.ndarray[np.int32_t, ndim=2] start_points,
                                   np.ndarray[np.int32_t, ndim=2] end_points,
                                   np.ndarray[np.int32_t, ndim=2] grid):
    cdef unsigned k, nrows
    cdef int x0, y0, x1, y1

    nrows = start_points.shape[0]

    for k in range(nrows):
        x0 = start_points[k, 0]
        y0 = start_points[k, 1]
        x1 = end_points[k, 0]
        y1 = end_points[k, 1]
        fill_grid_with_bresenham_line(x0, y0, x1, y1, grid)