// CBSE (Class 10) -- Q13: a line cutting a circle at two points is a ___
// OR: tangents at the ends of a diameter are ___
#include <stdio.h>

int main()
{
// circle x^2 + y^2 = 1 and line y = 0.5: x^2 = 1 - 0.5^2 > 0, so 2 points
double d = 0.5, r = 1;
printf("points = %d\n", (d*d < r*r) ? 2 : 0);

// ends of a diameter A = (1,0), B = (-1,0): tangent directions m = (-n2, n1)
int m1[2] = {0, 1}, m2[2] = {0, -1};
printf("cross = %d\n", m1[0]*m2[1] - m1[1]*m2[0]);   // 0, so parallel

return 0;
}
