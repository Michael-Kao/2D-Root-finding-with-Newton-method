#include <iostream>
#include <cmath>
#include <climits>
#include <fstream>

std::ofstream ofs;
/*
f(x, y) = x^2 + y^2 = 4
g(x, y) = x^2 - y^2 = 2
fx(x, y) = 2x
fy(x, y) = 2y
gx(x, y) = 2x
gy(x, y) = -2y
*/

double f(double x, double y) {
    return (x * x + y * y - 4);
}

double g(double x, double y) {
    return (x * x - y * y - 2);
}

double fx(double x) {
    return (2 * x);
}

double fy(double y) {
    return (2 * y);
}

double gx(double x) {
    return (2 * x);
}

double gy(double y) {
    return (-2 * y);
}

double determin(double x, double y) {
    return (1.0 / ((fy(y) * gx(x)) - (fx(x) * gy(y))));
}

double norm2(double x1, double y1, double x2, double y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

void newton2D(double x, double y) {
    double epsilon = 0.000001; // 10^-6
    double e = 1;
    int i = 1;
    while(e > epsilon) {
        double fval = f(x, y);
        double gval = g(x, y);
        double fxval = fx(x);
        double fyval = fy(y);
        double gxval = gx(x);
        double gyval = gy(y);
        double detval = determin(x, y);
        double h = detval * (gyval * fval - fyval * gval);
        double k = detval * ((-gxval * fval) + (fxval * gval));
        double xnew = x + h;
        double ynew = y + k;
        e = norm2(x, y, xnew, ynew);
        ofs << i << " : (" << x << "," << y << ")\n";
        x = xnew;
        y = ynew;
        i++;
    }
    ofs << "ans : (" << x << "," << y << ")\n";
}

int main() {
    ofs.open("result.txt", std::ios::trunc);
    if (!ofs.is_open())
    {
        std::cerr << "Failed to open the file!" << std::endl;
        return 1;
    }
    double perturbation = 0;
    ofs << "perturbation = " << perturbation << "\n";
    for(int i = -3; i < 4; i++) {
        for(int j = -3; j < 4; j++) {
            ofs << "------------------------------------------------------\n";
            double x = i + perturbation;
            double y = j + perturbation;
            newton2D(x, y);
            ofs << "------------------------------------------------------\n";
        }
    }
    ofs.close();
    return 0;
}
