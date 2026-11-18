#include <stdio.h>

int main(void)
{
  double low[6] = {25, 30, 35, 40, 45, 50};   /* lower class limits */
  double f[6]   = {20, 36, 53, 40, 28, 14};   /* frequencies */
  double h = 5;                               /* class width */

  /* modal class = class with the largest frequency */
  int m = 0;
  for (int i = 1; i < 6; i++)
    if (f[i] > f[m]) m = i;

  double f0 = f[m - 1], f1 = f[m], f2 = f[m + 1];

  /* mode = l + h (-f0 + f1) / (-f0 + 2 f1 - f2) */
  double mode = low[m] + h * (f1 - f0) / (2 * f1 - f0 - f2);

  printf("modal class = %g - %g\n", low[m], low[m] + h);
  printf("f0 = %g, f1 = %g, f2 = %g\n", f0, f1, f2);
  printf("mode = %.4f\n", mode);
  return 0;
}
