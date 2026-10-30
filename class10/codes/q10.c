// CBSE (Class 10) -- Q10: frustum of height 8 cm, radii 10 cm and 4 cm.
// Find the slant height.
#include <stdio.h>
#include <math.h>

int main()
{
double h = 8, R = 10, r = 4;

// l = sqrt(h^2 + (R - r)^2)
printf("l = %lf cm\n", sqrt(h*h + (R - r)*(R - r)));

return 0;
}
