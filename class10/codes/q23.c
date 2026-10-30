// CBSE (Class 10) -- Q23: solve 9x^2 - 6a^2 x + a^4 - b^4 = 0
// using the quadratic formula. Check with a = 2, b = 1
#include <stdio.h>
#include <math.h>

int main()
{
double a = 2, b = 1;
double A = 9, B = -6*a*a, C = pow(a, 4) - pow(b, 4);
double D = B*B - 4*A*C;                 // 36 b^4

// roots (a^2 + b^2)/3 and (a^2 - b^2)/3
printf("x = %lf, %lf\n", (-B + sqrt(D))/(2*A), (-B - sqrt(D))/(2*A));

return 0;
}
