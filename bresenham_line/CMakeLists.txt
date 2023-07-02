cmake_minimum_required(VERSION 3.10)
project(bresemham_line)

set(CMAKE_CXX_STANDARD 17)
set(CXX_STANDARD_REQUIRED ON)

# Build Release by default
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()
message("Build type: ${CMAKE_BUILD_TYPE}")

# More strict compile errors
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")

find_package(pybind11 REQUIRED)
find_package(Eigen3 REQUIRED)

include_directories(${EIGEN3_INCLUDE_DIR})

add_executable (sample bresemham_line_sample.cpp bresemham_line.cpp)


pybind11_add_module(example py_wrapper.cpp bresemham_line.cpp)
