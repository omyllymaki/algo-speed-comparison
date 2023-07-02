# algo-speed-comparison

Quick comparison of different line rasterization implementations.

Bresenham's line algorithm:
https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

Version C++ python binding: 6201472 lines per second
Version numba: 4548051 lines per second
Version cython: 1374280 lines per second
Version skimage: 38569 lines per second
Version python: 1857 lines per second