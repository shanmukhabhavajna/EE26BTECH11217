// q6.c  --  CBSE Class 10 Maths (Standard) 30/C/3, Q6
// mean = 10, median = 14, find the mode.   Empirical relation: mode = 3 median - 2 mean
// Written as a dot product  mode = w^T x,  w = [3, -2]^T,  x = [median, mean]^T
// Only the C standard library is used.
#include <stdio.h>

double dot(const double *a, const double *b, int n)
{
    double s = 0.0;
    for (int i = 0; i < n; i++)
        s += a[i] * b[i];
    return s;
}

int main(void)
{
    double mean = 10.0, median = 14.0;
    double w[2] = {3.0, -2.0};
    double x[2] = {median, mean};
    double mode = dot(w, x, 2);

    double opt[4] = {6.0, 22.0, 2.0, 20.0};
    const char *lab = "ABCD";

    printf("mean = %.2f, median = %.2f\n", mean, median);
    printf("mode = 3*median - 2*mean = %.2f\n", mode);
    for (int i = 0; i < 4; i++)
        printf("(%c) %.0f %s\n", lab[i], opt[i], opt[i] == mode ? "<-- answer" : "");

    return 0;
}
