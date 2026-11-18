#include <stdio.h>

long gcd(long x, long y)
{
  while (y != 0) {
    long t = x % y;
    x = y;
    y = t;
  }
  return x;
}

int main(void)
{
  long a = 2, b = 3;                 /* any two primes */
  long p = a * b * b * b;            /* p = a b^3 */
  long q = a * a * b;                /* q = a^2 b */

  long lcm = p * q / gcd(p, q);      /* LCM = pq / HCF */

  printf("LCM = %ld, a^2 b^3 = %ld\n", lcm, a * a * b * b * b);
  return 0;
}
