#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):

    count = 0
    store = dict()

    for x in A:
        if x in store:
            store[x] += 1
        else:
            store[x] = 1

    for y in B:
        if y in store:
            if store[y] > 0:
                store[y] -= 1
                count += 1

    if count == len(A):
        return count - 1
    else:
        return count + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
