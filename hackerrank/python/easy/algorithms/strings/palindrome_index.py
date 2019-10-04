#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if not s:
        return -1

    left = 0
    right = len(s) - 1
    index = -1

    while left < right:

        if s[left] != s[right]:
            if (left + 1 < right) and (s[left + 1] == s[right]) and (left < right - 1) and (s[left] == s[right - 1]):

                if (left + 2 < right - 1) and (s[left + 2] == s[right - 1]):
                    if index == -1:
                        index = left
                        left += 1
                    else:
                        return -1
                elif (left + 1 < right - 2) and (s[left + 1] == s[right - 2]):
                    if index == -1:
                        index = right
                        right -= 1
                    else:
                        return -1
                else:
                    return -1
            elif (left + 1 < right) and (s[left + 1] == s[right]):
                if index == -1:
                    index = left
                    left += 1
                else:
                    return -1
            elif (left < right - 1) and (s[left] == s[right - 1]):
                if index == -1:
                    index = right
                    right -= 1
                else:
                    return -1
            else:
                return -1

        left += 1
        right -= 1
    return index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
