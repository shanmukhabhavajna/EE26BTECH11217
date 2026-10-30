// CBSE (Class 10) -- Q15: alpha, beta are zeroes of 2x^2 - 5x - 4.
// Find 1/alpha + 1/beta
#include <stdio.h>

int main()
{
double a = 2, b = -5, c = -4;

// sum = -b/a, product = c/a, 1/alpha + 1/beta = sum/product
printf("value = %lf\n", (-b/a)/(c/a));

return 0;
}
