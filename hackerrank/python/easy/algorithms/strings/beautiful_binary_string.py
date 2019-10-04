#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulBinaryString(b):
  dig = 0
  count = 0

  for char in b:
    if char == '0':
        if dig == 2:
            count += 1
            dig = 0
        elif dig == 0:
            dig = 1        
    if char == '1':
        if dig == 2:
            dig = 0
        elif dig == 1:
          dig = 2

  return count 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
