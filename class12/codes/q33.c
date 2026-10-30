// Q33 (OR): cylinder of greatest curved surface area inside a cone
// Claim: the best radius of the cylinder is half the radius of the cone
#include <stdio.h>
#include <math.h>

int main()
{
    double R = 6.0;     // radius of the cone (any value works)
    double H = 9.0;     // height of the cone (any value works)
    double r, h, S;
    double best_r = 0, best_S = 0;

    // try many radii for the cylinder, from 0 to R
    for (r = 0; r <= R; r = r + 0.001)
    {
        h = H * (1 - r / R);        // height of cylinder (similar triangles)
        S = 2 * M_PI * r * h;       // curved surface area

        // keep the largest area found so far
        if (S > best_S)
        {
            best_S = S;
            best_r = r;
        }
    }

    printf("best r = %f\n", best_r);
    printf("R/2    = %f\n", R / 2);
    printf("max area = %f\n", best_S);
    printf("pi*R*H/2 = %f\n", M_PI * R * H / 2);

    return 0;
}
