// CBSE (Class 10) -- Q32: coin A has diameter 0.7 cm, B has double the diameter,
// and C, D onwards increase by 50%. Thickness is 0.25 cm, pi = 22/7.
// Find the diameter, area of one face and volume of each coin.
#include <stdio.h>

int main()
{
double pi = 22.0/7, t = 0.25;
double d[4] = {0.7, 1.4, 0, 0};
int i;

d[2] = 1.5*d[1];
d[3] = 1.5*d[2];

for(i = 0; i < 4; i++)
printf("%c: d = %lf, area = %lf, volume = %lf\n", 'A' + i, d[i], pi*d[i]*d[i]/4, pi*d[i]*d[i]/4*t);

return 0;
}
