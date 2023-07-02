#include "bresemham_line.h"

#include <iostream>
#include <fstream>
#include <string>
#include <Eigen/Dense>
#include <chrono>

using namespace std;
using namespace Eigen;

#define MAXBUFSIZE ((int)1e6)

MatrixXd readMatrix(const char *filename)
{
    int cols = 0, rows = 0;
    double buff[MAXBUFSIZE];

    // Read numbers from file into buffer.
    ifstream infile;
    infile.open(filename);
    while (!infile.eof())
    {
        string line;
        getline(infile, line);

        int temp_cols = 0;
        stringstream stream(line);
        while (!stream.eof())
            stream >> buff[cols * rows + temp_cols++];

        if (temp_cols == 0)
            continue;

        if (cols == 0)
            cols = temp_cols;

        rows++;
    }

    infile.close();

    rows--;

    // Populate matrix with numbers.
    MatrixXd result(rows, cols);
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            result(i, j) = buff[cols * i + j];

    return result;
}

int main()
{
    auto start_points = readMatrix("../../data/start_points_int.txt");
    auto end_points = readMatrix("../../data/end_points_int.txt");

    MatrixXi start_points_int = start_points.cast <int> ();
    MatrixXi end_points_int = end_points.cast <int> ();

    Eigen::MatrixXi grid;
    grid.resize(134, 134);

    auto startTime = std::chrono::high_resolution_clock::now();
    bresemham_line::fill_grid_with_bresenham_lines(start_points_int, end_points_int, grid);
    auto endTime = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endTime - startTime).count()/1000000.0;
    std::cout << duration << std::endl;
    size_t nLinesPerSecond = start_points_int.rows() / duration;
    std::cout << "Calculated " << nLinesPerSecond << " lines per second" << std::endl; 

    

    return 0;
}
