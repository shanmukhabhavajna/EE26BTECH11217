// CBSE (Class 10) -- Q21: show that any positive odd integer is of the form
// 4q + 1 or 4q + 3. Check for the odd integers below 100
#include <stdio.h>

int main()
{
int n, ok = 1;

// n = 4q + r with r = n mod 4, and q = n/4
for(n = 1; n < 100; n += 2)
if(n % 4 != 1 && n % 4 != 3)
ok = 0;

printf("all odd n are 4q+1 or 4q+3: %d\n", ok);

return 0;
}
