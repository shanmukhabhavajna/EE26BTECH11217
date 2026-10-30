// CBSE (Class 10) -- Q17: centre (4,4), one end of a diameter (4,0).
// Find the other end.
#include <stdio.h>

int main()
{
double O[2] = {4, 4}, A[2] = {4, 0};

// O is the midpoint of AB, so B = 2O - A
printf("B = (%lf, %lf)\n", 2*O[0] - A[0], 2*O[1] - A[1]);

return 0;
}
