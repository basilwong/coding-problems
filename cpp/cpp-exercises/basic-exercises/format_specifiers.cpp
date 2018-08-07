#include <iostream>
#include <cstdio>
#include "functions.h"

using namespace std;
// Input consists of the following space-separated values: int, long, char, float, and double, respectively.

void format_specifiers(){

    int a;
    long b;
    char c;
    float d;
    double e;

    scanf("%i %li %c %f %lf", &a, &b ,&c, &d, &e);
    printf("%i\n%li\n%c\n%.03f\n%.09lf\n",a,b,c,d,e);
    printf("%i",a);

}

//int main() {
//  format_specifiers();
//  return 0;
//}

