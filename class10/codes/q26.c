// CBSE (Class 10) -- Q26: find the mode of the grouped distribution
// classes 25-30, ..., 50-55 with frequencies 20, 36, 53, 40, 28, 14
#include <stdio.h>

int main()
{
double f[6] = {20, 36, 53, 40, 28, 14};
double l = 25, h = 5;
int i, m = 0;

// modal class has the largest frequency
for(i = 1; i < 6; i++)
if(f[i] > f[m])
m = i;

// mode = l + (f1 - f0)/(2 f1 - f0 - f2) h
l = l + m*h;
printf("mode = %lf\n", l + (f[m] - f[m-1])/(2*f[m] - f[m-1] - f[m+1])*h);

return 0;
}
