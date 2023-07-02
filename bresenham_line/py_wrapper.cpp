#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <Eigen/LU>
#include "bresemham_line.h"

namespace py = pybind11;

PYBIND11_MODULE(example, m) {
    m.doc() = "optional module docstring";
    m.def("rasterize_lines", &rasterize_lines, "A function that rasterizes the lines with Bresemham's line algorithm.");
}