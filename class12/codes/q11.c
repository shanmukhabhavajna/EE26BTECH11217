//CBSE 65-C-3 (Class 12) -- Q11
//(a) A square matrix A is singular if |A| = 0
//(b) OR: A = [3 -5; 2 0], B = [1 17; 0 -10], find |AB|
//Uses matgeo's matfun.h
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"

int main()
{
double **S, **A, **B, **AB;

//(a) a singular matrix has zero determinant
S = createMat(2,2);
S[0][0] = 1; S[0][1] = 2;
S[1][0] = 2; S[1][1] = 4;
printf("Q11(a): |S| = %lf\n", Matdet(S));   //0, so S is singular

//(b) |AB|
A = createMat(2,2);
B = createMat(2,2);
A[0][0] = 3; A[0][1] = -5;
A[1][0] = 2; A[1][1] = 0;
B[0][0] = 1; B[0][1] = 17;
B[1][0] = 0; B[1][1] = -10;

AB = Matmul(A,B,2,2,2);
printf("Q11(b): AB =\n");
printMat(AB,2,2);
printf("Q11(b): |A| = %lf, |B| = %lf\n", Matdet(A), Matdet(B));
printf("Q11(b): |AB| = %lf\n", Matdet(AB));                   //-100
printf("Q11(b): |A||B| = %lf\n", Matdet(A)*Matdet(B));        //-100

return 0;
}
