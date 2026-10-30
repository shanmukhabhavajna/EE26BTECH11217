// CBSE (Class 10) -- Q8: 3x^2 - kx + 3 = 0 has equal roots. Find k.
// OR: find the discriminant of 3sqrt(3)x^2 + 10x + sqrt(3) = 0
#include <stdio.h>
#include <math.h>

int main()
{
double a = 3, c = 3;
double a2 = 3*sqrt(3), b2 = 10, c2 = sqrt(3);

// equal roots: k^2 - 4ac = 0
printf("k = +-%lf\n", sqrt(4*a*c));

// discriminant = b^2 - 4ac
printf("D = %lf\n", b2*b2 - 4*a2*c2);

return 0;
}
