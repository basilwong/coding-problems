#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    half = len(s) // 2
    #Check for impossible case
    if len(s) % 2 != 0:
        return -1

    # Split string down the middle
    a = s[:half]
    b = s[half:]

    # Create/populate hashtable with a
    ht = dict()
    for i in a:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1
    print(ht)
    # Count changes to b
    count = 0
    for j in b:
        if j in ht and ht[j] != 0:
                ht[j] -= 1
                count += 1

    # # Add changes to a
    # for letter in ht:
    #     count += ht[letter]

    return half - count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
