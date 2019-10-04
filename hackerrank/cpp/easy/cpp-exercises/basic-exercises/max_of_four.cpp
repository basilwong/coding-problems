#include <iostream>
#include <cstdio>
#include "functions.h"
using namespace std;

int max_of_four(int a, int b, int c, int d){
    int list[] = {a, b, c, d};

    int large = 0;

    for (int i = 0; i <= 3; i++){
        if (list[i] > large){
            large = list[i];
        }

    }

    return large;
}

//int main() {
//    int a, b, c, d;
//    scanf("%d %d %d %d", &a, &b, &c, &d);
//    int ans = max_of_four(a, b, c, d);
//    printf("%d", ans);
//
//    return 0;
//}
