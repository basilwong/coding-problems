#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):

  arr.sort()
  count = 0
  val = 0
  left = len(arr)
  ret = []
  print(arr)
  for i in range(len(arr)):
    if arr[i] > val:
      left -= count
      ret.append(left)
      count = 1
      val = arr[i]
    else:
      count += 1
  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
