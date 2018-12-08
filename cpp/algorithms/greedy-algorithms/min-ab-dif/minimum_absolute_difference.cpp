#include "ab_dif.h"
#include <vector>
#include <cstdlib>
#include <iostream>

int minimumAbsoluteDifference(std::vector<int> arr) {

  int min = 100000000;
  int val;
  int abs_val;

  for (int i = 0; i < arr.size(); i++) {
    for (int j = i + 1; j < arr.size(); j++) {
      val = arr[i] - arr[j];
      abs_val = std::abs(val);
      if (abs_val < min) {
        min = abs_val;
      }
    }
  }
  return min;
}
