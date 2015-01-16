cmake_minimum_required (VERSION 2.8.9)
project (warde-algorithm)

set(CMAKE_CXX_FLAGS "-std=c++0x -D_GLIBCXX_USE_NANOSLEEP -Wall -pedantic ${CMAKE_CXX_FLAGS}")

set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(test main.cpp)
add_executable(data-generator data_generator.cpp)
