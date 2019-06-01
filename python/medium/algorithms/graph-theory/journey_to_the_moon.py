#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    
    #construct 2d array of 
    pairs = list()

    for _ in range(n):
        pairs.append(set())

    for dude in astronaut:
        pairs[dude[0]].add(dude[1])
        pairs[dude[1]].add(dude[0])

    # Visited set 
    visited = set()

    # Number of non-pairs
    non_pairs = 0

    for i in range(n):
        if i not in visited:
            visited.add(i)
            visited.update(pairs[i])
            non_pairs += (len(pairs[i]) + 1) * (len(pairs[i])) / 2

    ret = (n*(n-1) / 2) - non_pairs

    return int(ret)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

