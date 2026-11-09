// q40.c  --  CBSE Class 10 Maths (Standard) 30/C/3, Q40
// 'less than' ogive of the given distribution and its median.
// The median is the abscissa of the point of the ogive with cumulative frequency N/2,
// found by Newton-Raphson on the linear piece of the ogive (polyline).
// The figure is written directly as an SVG file to ../figs/q40.svg (run from the codes folder).
// Only the C standard library is used.
#include <stdio.h>
#include <math.h>

#define NC 7
#define W 600
#define H 440
#define XMIN 20.0
#define XMAX 90.0
#define YMIN 0.0
#define YMAX 100.0
static double sx(double x) { return 70 + (x - XMIN) / (XMAX - XMIN) * (W - 100); }
static double sy(double y) { return H - 50 - (y - YMIN) / (YMAX - YMIN) * (H - 80); }

int main(void)
{
    double lo[NC] = {20, 30, 40, 50, 60, 70, 80};     // lower class limits
    double h = 10.0;                                   // class width
    double fr[NC] = {10, 8, 12, 24, 6, 25, 15};        // frequencies

    double cf[NC + 1], x[NC + 1];                      // ogive points (upper limit, cum. freq.)
    x[0] = lo[0];
    cf[0] = 0.0;
    for (int i = 0; i < NC; i++) {
        x[i + 1] = lo[i] + h;
        cf[i + 1] = cf[i] + fr[i];
    }
    double N = cf[NC];
    double half = N / 2.0;

    printf("upper limit   cumulative frequency\n");
    for (int i = 0; i <= NC; i++)
        printf("%8.0f %12.0f\n", x[i], cf[i]);
    printf("N = %.0f, N/2 = %.1f\n", N, half);

    // locate the segment of the ogive that contains N/2
    int k = 0;
    while (cf[k + 1] < half)
        k++;
    double slope = (cf[k + 1] - cf[k]) / (x[k + 1] - x[k]);   // linear piece: F(t) = cf[k] + slope (t - x[k])
    double t = 0.5 * (x[k] + x[k + 1]);
    for (int i = 0; i < 20; i++) {                    // Newton-Raphson on F(t) - N/2 = 0
        double g = cf[k] + slope * (t - x[k]) - half;
        double tn = t - g / slope;
        if (fabs(tn - t) < 1e-12) { t = tn; break; }
        t = tn;
    }
    printf("median class: %.0f - %.0f\n", x[k], x[k + 1]);
    printf("median (from ogive) = %.4f\n", t);
    printf("median (formula l + (N/2 - cf)/f * h) = %.4f\n", x[k] + (half - cf[k]) / fr[k] * h);

    // ---- figure: 'less than' ogive with the median ----
    FILE *fp = fopen("../figs/q40.svg", "w");
    fprintf(fp, "<svg xmlns='http://www.w3.org/2000/svg' width='%d' height='%d'>\n", W, H);
    fprintf(fp, "<rect width='%d' height='%d' fill='white'/>\n", W, H);
    for (int v = 20; v <= 90; v += 10) {
        fprintf(fp, "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='#ddd'/>\n", sx(v), sy(YMIN), sx(v), sy(YMAX));
        fprintf(fp, "<text x='%g' y='%g' font-size='12' text-anchor='middle'>%d</text>\n", sx(v), sy(YMIN) + 16, v);
    }
    for (int v = 0; v <= 100; v += 20) {
        fprintf(fp, "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='#ddd'/>\n", sx(XMIN), sy(v), sx(XMAX), sy(v));
        fprintf(fp, "<text x='%g' y='%g' font-size='12' text-anchor='end'>%d</text>\n", sx(XMIN) - 6, sy(v) + 4, v);
    }
    fprintf(fp, "<polyline fill='none' stroke='blue' stroke-width='2' points='");
    for (int i = 0; i <= NC; i++)
        fprintf(fp, "%g,%g ", sx(x[i]), sy(cf[i]));
    fprintf(fp, "'/>\n");
    for (int i = 0; i <= NC; i++)
        fprintf(fp, "<circle cx='%g' cy='%g' r='4' fill='blue'/>\n", sx(x[i]), sy(cf[i]));
    fprintf(fp, "<polyline fill='none' stroke='red' stroke-dasharray='6,4' points='%g,%g %g,%g %g,%g'/>\n",
            sx(XMIN), sy(half), sx(t), sy(half), sx(t), sy(0));
    fprintf(fp, "<circle cx='%g' cy='%g' r='5' fill='red'/>\n", sx(t), sy(half));
    fprintf(fp, "<text x='%g' y='%g' font-size='13' fill='red'>median = %.2f</text>\n", sx(t) + 6, sy(0) - 8, t);
    fprintf(fp, "<text x='%g' y='%g' font-size='13' text-anchor='middle'>upper class limit</text>\n", sx(55), H - 8.0);
    fprintf(fp, "<text x='14' y='%g' font-size='13' transform='rotate(-90 14 %g)' text-anchor='middle'>cumulative frequency</text>\n", sy(50), sy(50));
    fprintf(fp, "</svg>\n");
    fclose(fp);
    return 0;
}
