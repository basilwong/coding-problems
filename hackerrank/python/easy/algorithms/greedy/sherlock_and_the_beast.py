#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):

    res = list()

    fives = n // 3

    for i in range(fives, -1, -1):
        if (n - (i * 3)) % 5 == 0:
            first = "5" * (i * 3)
            second = "3" * (n - (i * 3))
            print(first + second)
            return
    print("-1")
    return

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
 
