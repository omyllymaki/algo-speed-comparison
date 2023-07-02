# algo-speed-comparison

Quick comparison of different line rasterization implementations.

Bresenham's line algorithm:
https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

Different implmentations:
- C++ python binding: 6201472 lines per second
- numba: 4548051 lines per second
- cython: 1374280 lines per second
- skimage: 38569 lines per second
- Pure python: 1857 lines per second