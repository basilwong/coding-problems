#!/bin/python3

import math
import os
import random
import re
import sys

# Unicode representation
# a = 97
# z = 122
# A = 65
# Z = 90
def rotate_letter(char, k):
    temp = ord(char)
    if temp >= 97 and temp <= 122: # lowercase
        hrd = 97
    elif temp >= 65 and temp <= 90: # uppercase
        hrd = 65
    else:
        return char

    return chr(hrd + (temp - hrd + k) % 26)


def caesarCipher(s, k):

    g = list(s)

    for i in range(len(g)):
        g[i] = rotate_letter(g[i], k)

    return "".join(g)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
