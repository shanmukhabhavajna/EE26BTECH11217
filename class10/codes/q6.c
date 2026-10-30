// CBSE (Class 10) -- Q6: mean = 10, median = 14. Find the mode.
#include <stdio.h>

int main()
{
double mean = 10, median = 14, mode;

// 3 median = mode + 2 mean
mode = 3*median - 2*mean;

printf("mode = %lf\n", mode);

return 0;
}
