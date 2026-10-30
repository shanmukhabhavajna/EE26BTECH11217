// CBSE (Class 10) -- Q19: triangle ABC ~ triangle PQR, BC/QR = 1/3.
// Find ar(PRQ)/ar(ACB)
#include <stdio.h>

int main()
{
double k = 1.0/3;

// ar(ABC)/ar(PQR) = k^2, so the required ratio is 1/k^2
printf("ratio = %lf\n", 1/(k*k));

return 0;
}
