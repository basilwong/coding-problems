#include "lower_bound.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
 * You are given N integers in the sorted order. Then you are given Q queries. In each query you will be given an int
 * and you have to tell whether that integer is present in the array, if so you have to tell at which index it is
 * present and if it is not present you have to tell the index at which the smallest integer that is just greater than
 * the given number is present.
 * */

void lower_bound() {

  // Retrieving N.
  int N;
  cin >> N;
  // Retrieving sorted vector.
  vector< int > sorted;
  int temp;
  for (int i = 0; i < N; i++) {
    cin >> temp;
    sorted.push_back(temp);
  }

  // Retrieving Q.
  int Q;
  cin >> Q;
  // Responding to queries.
  int query;
  for (int j = 0; j < Q; j++) {
    cin >> query;
    vector<int>::iterator low = lower_bound(sorted.begin(), sorted.end(), query);
    if (sorted[low - sorted.begin()] == query) {
      cout << "Yes " << (low - sorted.begin() + 1) << endl;
    } else {
      cout << "No " << (low - sorted.begin() + 1) << endl;
    }
  }

}

/*
 8
 1 1 2 2 6 9 9 15
 4
 1
 4
 9
 15
 */