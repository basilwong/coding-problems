#!/bin/python3

import math
import os
import random
import re
import sys

# Time Complexity: O(nlogn), Space Complexity: O(1)
def toys1(w):
    w.sort()

    count = 1
    cur = w[0]
    for i in range(1,len(w)):
        if w[i] > cur + 4:
            count += 1
            cur = w[i]

    return count

# Time Complexity: O(max(n, max(w)))
# Space Complexity: O(n)
def toys2(w):

    hashset = set(w)
    count = 0
    max_w = max(w)

    i = 0
    while i <= max_w:
        if i in hashset:
            count += 1
            i += 4
        i += 1
    return count
