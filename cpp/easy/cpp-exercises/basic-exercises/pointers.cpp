#include <stdio.h>
#include <stdlib.h>
#include "functions.h"

//complete the function void update(int *a,int *b), which reads two integers as
//argument, and sets a with the sum of them, and b with the absolute difference
//of them.

void pointers(int *a,int *b) {
  int sum_temp = *a + *b;
  int minus_temp = abs(*a - *b);

  *a = sum_temp;
  *b = minus_temp;
}

//int main() {
//    int a, b;
//    int *pa = &a, *pb = &b;
//
//    scanf("%d %d", &a, &b);
//    update(pa, pb);
//    printf("%d\n%d", a, b);
//
//    return 0;
//}
