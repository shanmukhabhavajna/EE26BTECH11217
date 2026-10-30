// CBSE (Class 10) -- Q38: A and B together finish a work in 15 days. A alone takes
// 16 days less than B. Find the number of days B takes.
#include <stdio.h>
#include <math.h>

int main()
{
// B takes x days: 1/x + 1/(x - 16) = 1/15 gives x^2 - 46x + 240 = 0
double a = 1, b = -46, c = 240;
double D = b*b - 4*a*c;

// the root 6 is rejected since A would take 6 - 16 < 0 days
printf("B takes %lf days\n", (-b + sqrt(D))/(2*a));

return 0;
}
