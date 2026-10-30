// CBSE (Class 10) -- Q14: (0,0), (2m,-4), (3,6) are collinear. Find m.
#include <stdio.h>

int main()
{
// det [2m 3; -4 6] = 12m + 12 = 0
double m = -12.0/12.0;
double det = 2*m*6 - 3*(-4);

printf("m = %lf, det = %lf\n", m, det);

return 0;
}
