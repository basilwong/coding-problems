#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
  arr = list(s)
  arr = [ord(i) for i in arr]
  changes = 0
  for c in range(int(len(arr)/2)):
    changes += abs(arr[c] - arr[len(arr) - c - 1])

  return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
