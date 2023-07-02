#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <Eigen/LU>
#include "bresemham_line.h"

namespace py = pybind11;

PYBIND11_MODULE(line_rasterization_module, m) {
    m.def("rasterize_lines", &rasterize_lines, "A function that rasterizes the lines with Bresemham's line algorithm.");
}