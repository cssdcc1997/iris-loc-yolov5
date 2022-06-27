cmake_minimum_required(VERSION 2.8.12)

project(iris_location)

set(CMAKE_CXX_STANDARD 14)

add_executable(${PROJECT_NAME} yolov5.cpp)

find_package(OpenCV REQUIRED)
message("find opencv succeed")
find_package(ncnn REQUIRED)

FIND_PACKAGE( OpenMP REQUIRED)
if (OPENMP_FOUND)
    message("OPENMAP FOUND")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
include_directories(/home/cssdcc/software/ncnn/build/install/include/ncnn)
link_directories(/home/cssdcc/software/ncnn/install/lib)
# add_subdirectory(src)

target_link_libraries(${PROJECT_NAME}
    ${OpenCV_LIBS}
    ncnn
)