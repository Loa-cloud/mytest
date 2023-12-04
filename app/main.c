#include <stdio.h>

#include "myfunc.h"

int main()
{
    double a, b, c, x1, x2;

    a = 2;
    b = 7;
    c = 32;

    //printf("Enter a:\n");
    //scanf_s("%lf", &a);
    //printf("Hello World!\n");
    //return myfunc(2);
    root(a, b, c, &x1, &x2);
    printf("x1: %lf, x2: %lf\n", x1, x2);
    return 0;
}
