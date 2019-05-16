#!/bin/python3

import math
import os
import random
import re
import sys

def gemstones(arr):
  gems = set()
  accounted = set()

  if not arr:
    return 0

  for x in arr[0]:
    gems.add(x)
  for rock in arr:
    for mineral in rock:
      accounted.add(mineral)
    gems.intersection_update(accounted)
    accounted.clear()
  
  return len(gems)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
