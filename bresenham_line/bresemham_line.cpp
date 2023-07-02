#include "bresemham_line.h"
#include <iostream>
#include <cmath>

void bresemham_line::fill_grid_with_bresenham_line(size_t x0, size_t y0, size_t x1, size_t y1, Eigen::MatrixXi &grid)
{
    int e2, sx, sy, error;
    int dx, dy;

    dx = abs(static_cast<int>(x1 - x0));
    sx = (x0 < x1) ? 1 : -1;
    dy = -abs(static_cast<int>(y1 - y0));
    sy = (y0 < y1) ? 1 : -1;
    error = dx + dy;

    while (true)
    {
        grid(x0, y0) += 1;
        if ((x0 == x1) & (y0 == y1))
        {
            break;
        }
        e2 = 2 * error;
        if (e2 >= dy)
        {
            if (x0 == x1)
            {
                break;
            }

            error = error + dy;
            x0 = x0 + sx;
        }
        if (e2 <= dx)
        {
            if (y0 == y1)
            {
                break;
            }
            error = error + dx;
            y0 = y0 + sy;
        }
    }
}

void bresemham_line::fill_grid_with_bresenham_lines(const Eigen::MatrixX2i &start_points,
                                                    const Eigen::MatrixX2i &end_points,
                                                    Eigen::MatrixXi &grid)
{
    size_t nRows = start_points.rows();
    for (size_t i = 0; i < nRows; i++)
    {
        size_t x0 = start_points.coeff(i, 0);
        size_t y0 = start_points.coeff(i, 1);
        size_t x1 = end_points.coeff(i, 0);
        size_t y1 = end_points.coeff(i, 1);
        fill_grid_with_bresenham_line(x0, y0, x1, y1, grid);
    }
}