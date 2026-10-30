#include <stdio.h>
#include <math.h>
 
int main()
{
double A, B, C;
 
//cot^-1(x) = atan(1/x) for x > 0
A = atan(1.0/2.0);
B = atan(1.0/3.0);
 
//tan(A+B) = (tanA + tanB)/(1 - tanA tanB)
               //pi/4
 
//sum of angles of a triangle is pi
C = M_PI - A - B;
printf("third angle = %lf rad" ,C);
//3pi/4 = 2.356194 rad = 0.75 pi = 135 deg
 
return 0;
}
 
