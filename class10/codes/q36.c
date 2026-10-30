// CBSE (Class 10) -- Q36: from the top of a 60 sqrt(3) m cliff, the angles of
// depression of the top and bottom of a tower are 45 and 60 degrees.
// Find the height of the tower. (sqrt(3) = 1.73)
#include <stdio.h>

int main()
{
double s3 = 1.73;
double H = 60*s3;

// tan 60 = H/d gives d, tan 45 = (H - h)/d gives h
double d = H/s3;
double h = H - d;

printf("h = %lf m\n", h);

return 0;
}
