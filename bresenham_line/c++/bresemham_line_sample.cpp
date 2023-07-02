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
    auto start_points = readMatrix("../../../data/start_points_int.txt");
    auto end_points = readMatrix("../../../data/end_points_int.txt");

    MatrixXi start_points_int = start_points.cast<int>();
    MatrixXi end_points_int = end_points.cast<int>();

    auto start_time = std::chrono::high_resolution_clock::now();
    auto grid = rasterize_lines(start_points_int, end_points_int, {134, 134});
    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count() / 1000000.0;
    size_t n_lines_per_second = start_points_int.rows() / duration;
    std::cout << "Calculated " << n_lines_per_second << " lines per second" << std::endl;

    return 0;
}
