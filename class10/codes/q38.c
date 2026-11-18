// q38.c  --  CBSE Class 10 Maths (Standard) 30/C/3, Q38
// A and B together finish a work in 15 days; A alone takes 16 days less than B.
// If A takes x days, B takes x + 16 days:
//      1/x + 1/(x+16) = 1/15   =>   f(x) = x^2 - 14 x - 240 = 0
// solved with the Newton-Raphson method.
// The figure is written directly as an SVG file to ../figs/q38.svg (run from the codes folder).
// Only the C standard library is used.
#include <stdio.h>
#include <math.h>

#define W 600
#define H 420
#define XMIN (-20.0)
#define XMAX 40.0
#define YMIN (-300.0)
#define YMAX 800.0
static double sx(double x) { return 70 + (x - XMIN) / (XMAX - XMIN) * (W - 100); }
static double sy(double y) { return H - 50 - (y - YMIN) / (YMAX - YMIN) * (H - 80); }

double f(double x)  { return x * x - 14.0 * x - 240.0; }
double df(double x) { return 2.0 * x - 14.0; }

double newton(double x0, double tol, int maxit)
{
    double x = x0;
    for (int i = 0; i < maxit; i++) {
        double xn = x - f(x) / df(x);
        printf("  iter %2d: x = %.10f\n", i + 1, xn);
        if (fabs(xn - x) < tol)
            return xn;
        x = xn;
    }
    return x;
}

int main(void)
{
    printf("Newton-Raphson from x0 = 30\n");
    double xa = newton(30.0, 1e-12, 50);
    printf("Newton-Raphson from x0 = -20\n");
    double xn = newton(-20.0, 1e-12, 50);

    double A = xa, B = xa + 16.0;               // x > 0 is the only admissible root
    printf("roots: %.6f and %.6f (negative root rejected)\n", xa, xn);
    printf("A alone = %.4f days, B alone = %.4f days\n", A, B);
    printf("check 1/A + 1/B = %.6f, 1/15 = %.6f\n", 1.0 / A + 1.0 / B, 1.0 / 15.0);

    // ---- figure: f(x) = x^2 - 14x - 240 ----
    FILE *fp = fopen("../figs/q38.svg", "w");
    fprintf(fp, "<svg xmlns='http://www.w3.org/2000/svg' width='%d' height='%d'>\n", W, H);
    fprintf(fp, "<rect width='%d' height='%d' fill='white'/>\n", W, H);
    for (int t = -20; t <= 40; t += 10) {        // x grid and labels
        fprintf(fp, "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='#ddd'/>\n", sx(t), sy(YMIN), sx(t), sy(YMAX));
        fprintf(fp, "<text x='%g' y='%g' font-size='12' text-anchor='middle'>%d</text>\n", sx(t), sy(YMIN) + 16, t);
    }
    for (int t = -200; t <= 800; t += 200) {     // y grid and labels
        fprintf(fp, "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='#ddd'/>\n", sx(XMIN), sy(t), sx(XMAX), sy(t));
        fprintf(fp, "<text x='%g' y='%g' font-size='12' text-anchor='end'>%d</text>\n", sx(XMIN) - 6, sy(t) + 4, t);
    }
    fprintf(fp, "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='black'/>\n", sx(XMIN), sy(0), sx(XMAX), sy(0));
    fprintf(fp, "<polyline fill='none' stroke='#1f77b4' stroke-width='2' points='");
    for (double x = XMIN; x <= XMAX + 1e-9; x += 0.5)
        fprintf(fp, "%g,%g ", sx(x), sy(f(x)));
    fprintf(fp, "'/>\n");
    fprintf(fp, "<circle cx='%g' cy='%g' r='5' fill='red'/>\n<circle cx='%g' cy='%g' r='5' fill='red'/>\n", sx(xa), sy(0), sx(xn), sy(0));
    fprintf(fp, "<text x='%g' y='%g' font-size='13' text-anchor='middle'>x = %g (A)</text>\n", sx(xa), sy(0) - 12, xa);
    fprintf(fp, "<text x='%g' y='%g' font-size='13' text-anchor='middle'>x = %g (rejected)</text>\n", sx(xn), sy(0) - 12, xn);
    fprintf(fp, "<text x='%g' y='%g' font-size='13' text-anchor='middle'>x (days taken by A)</text>\n", sx(10), H - 8.0);
    fprintf(fp, "<text x='14' y='%g' font-size='13' transform='rotate(-90 14 %g)' text-anchor='middle'>f(x) = x^2 - 14x - 240</text>\n", sy(250), sy(250));
    fprintf(fp, "</svg>\n");
    fclose(fp);
    return 0;
}
