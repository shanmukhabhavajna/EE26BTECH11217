// CBSE (Class 10) -- Q37: a well of diameter 3 m is dug 14 m deep. The earth is spread
// as a ring of width 4 m around it. Find the height of the platform. (pi = 22/7)
// OR: toy = cone (height 2 cm) on a hemisphere, base diameter 4 cm. Find the volume. (pi = 3.14)
#include <stdio.h>

int main()
{
double pi = 22.0/7;

// volume of earth = pi r^2 h, ring has inner radius 1.5 and outer radius 1.5 + 4
double V = pi*1.5*1.5*14;
printf("H = %lf m\n", V/(pi*(5.5*5.5 - 1.5*1.5)));

// OR: V = (1/3) pi r^2 h + (2/3) pi r^3
double p = 3.14, r = 2, h = 2;
printf("V = %lf cm^3\n", p*r*r*h/3 + 2*p*r*r*r/3);

return 0;
}
