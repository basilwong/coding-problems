#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
# Assumes k is smaller than the length of arr
def maxMin(k, arr):
  arr.sort()

  min_dex = 0
  optimal_dif = arr[k - 1] - arr[0]

  for i in range(k, len(arr)):
    if (arr[i] - arr[i - k + 1]) < optimal_dif:
      optimal_dif = arr[i] - arr[i - k + 1]
      min_dex = i - k + 1

  return arr[min_dex + k - 1] - arr[min_dex]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
