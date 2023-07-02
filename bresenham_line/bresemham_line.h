#ifndef BRESEMHAM_LINE_H
#define BRESEMHAM_LINE_H

#include <Eigen/Dense>

namespace bresemham_line
{

    void fill_grid_with_bresenham_line(size_t x0, size_t y0, size_t x1, size_t y1, Eigen::MatrixXi &grid);

    Eigen::MatrixXi rasterize_lines(const Eigen::MatrixX2i &start_points,
                                    const Eigen::MatrixX2i &end_points,
                                    const std::pair<size_t, size_t> &grid_dim);

}

#endif