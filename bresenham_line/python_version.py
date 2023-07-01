def fill_grid_with_bresenham_line(x0, y0, x1, y1, grid):
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
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


def fill_grid_with_bresenham_lines(start_points, end_points, grid):
    for i in range(start_points.shape[0]):
        sp = start_points[i]
        ep = end_points[i]
        fill_grid_with_bresenham_line(sp[0], sp[1], ep[0], ep[1], grid)
