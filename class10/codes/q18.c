// CBSE (Class 10) -- Q18: p = ab^3, q = a^2 b, a and b prime. Find LCM(p,q).
// Check with a = 2, b = 3
#include <stdio.h>

int gcd(int x, int y)
{
return y == 0 ? x : gcd(y, x % y);
}

int main()
{
int a = 2, b = 3;
int p = a*b*b*b, q = a*a*b;

// LCM = pq/gcd, and a^2 b^3 = 108
printf("LCM = %d, a^2 b^3 = %d\n", p*q/gcd(p, q), a*a*b*b*b);

return 0;
}
