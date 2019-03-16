#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include "functions.h"

using namespace std;

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    pointers(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
