#include "ab_dif.h"
#include <vector>
#include <cstdlib>
#include <iostream>
#include <algorithm>

// Sorts the vector then finds the absolute minimum difference in the vector
// by finding the absolute difference between each pair of adjacent elements. 
int minimumAbsoluteDifference(std::vector<int> arr) {

  int abs_val;

  std::sort(arr.begin(), arr.end());

  int min = std::abs(arr[0] - arr[1]);

  for (int i = 1; i < arr.size() - 1; i++) {
    abs_val = std::abs(arr[i] - arr[i+1]);
    if (min > abs_val) {
      min = abs_val;
    }
  }

  return min;
}
