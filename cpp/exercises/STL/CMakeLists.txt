cmake_minimum_required(VERSION 3.10)
project(STL)

set(CMAKE_CXX_STANDARD 11)

add_executable(STL main.cpp vector_sort.cpp vector_sort.h vector_erase.cpp vector_erase.h lower_bound.cpp lower_bound.h maps.cpp maps.h sets.cpp sets.h)