// CBSE (Class 10) -- Q40: draw the 'less than' ogive of the distribution and find the median.
// classes 20-30, ..., 80-90 with frequencies 10, 8, 12, 24, 6, 25, 15
#include <stdio.h>

int main()
{
double ub[7] = {30, 40, 50, 60, 70, 80, 90};
double f[7] = {10, 8, 12, 24, 6, 25, 15};
double cf[7], N = 0, h = 10;
int i;

// 'less than' ogive points are (ub, cf)
for(i = 0; i < 7; i++)
{
N += f[i];
cf[i] = N;
}

// the point with y = N/2 lies in the first class with cf >= N/2
i = 0;
while(cf[i] < N/2)
i++;

// median = l + (N/2 - cf before)/f * h
printf("N = %lf, median = %lf\n", N, ub[i] - h + (N/2 - (cf[i] - f[i]))/f[i]*h);

return 0;
}
