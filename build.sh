#!/usr/bin/env bash
echo "Build Cython"
echo "Build Cython version"
cd bresenham_line/cython
./build.sh
echo "Build C++ version"
cd ..
cd c++
mkdir build
cd build
cmake ..
make -j 4
echo "Done!"
