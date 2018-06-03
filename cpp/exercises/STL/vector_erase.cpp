#include "vector_erase.h"
#include <vector>
#include <iostream>
/*
 * You are provided with a vector of N integers. Then, you are given  queries. For the first query, you are provided with
 * integer, which denotes a position in the vector. The value at this position in the vector needs to be erased. The
 * next query consists of N integers denoting a range of the positions in the vector. The elements which fall under that
 * range should be removed. The second query is performed on the updated vector which we get after performing the first
 * query.
 */

void vector_erase(){

    int N;
    int temp;
    std::vector< int > vec;

    // Getting the vector contents.
    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> temp;
        vec.push_back(temp);
    }

    int first_q;

    // First Query
    std::cin >> first_q;

    vec.erase(vec.begin() + first_q - 1);

    // Second Query
    int second_q1, second_q2;

    std::cin >> second_q1 >> second_q2;

    vec.erase((vec.begin() + second_q1 - 1), (vec.begin() + second_q2 - 1));

    // Outputting size of the vector.
    std::cout << vec.size() << std::endl;

    // Outputting the contents of the new vector.
    for (auto it=vec.begin(); it!=vec.end(); ++it) {
        std::cout << *it << " ";
    }

}