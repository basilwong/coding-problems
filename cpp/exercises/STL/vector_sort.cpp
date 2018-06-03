#include "vector_sort.h"
#include <iostream>
#include <algorithm>
#include <vector>

/*
5
1 6 10 8 4
 */
void vector_sort() {

    int N;
    int temp;
    std::vector< int > vec_sort;

    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> temp;
        vec_sort.push_back(temp);
    }

    std::sort (vec_sort.begin(), vec_sort.end());

    for (int j = 0; j < N; j++) {
        std::cout << vec_sort[j] << " ";
    }
}