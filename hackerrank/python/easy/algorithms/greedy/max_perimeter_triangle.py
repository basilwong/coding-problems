#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
  sticks.sort()
  v1 = len(sticks) - 1
  v2 = v1 - 1
  v3 = v2 - 1
  while (sticks[v2] + sticks[v3]) <= sticks[v1]:
    v1 -= 1
    v2 -= 1
    v3 -= 1
    if v3 < 0:
      return [-1]

  return [sticks[v3], sticks[v2], sticks[v1]]





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
