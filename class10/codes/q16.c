// CBSE (Class 10) -- Q16: V = 125.6 cm^3, r = 2 cm, pi = 3.14. Find the height.
#include <stdio.h>

int main()
{
double V = 125.6, r = 2, pi = 3.14;

// V = pi r^2 h
printf("h = %lf cm\n", V/(pi*r*r));

return 0;
}
