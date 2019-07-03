#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the jimOrders function below.
def jimOrders(orders):

    minheap = list()

    # Add all the sums of order# and prep time to minheap corresponding to order#
    for i in range(len(orders)):
        heapq.heappush(minheap, ((orders[i][0] + orders[i][1]), i))

    minheap2 = list()
    ret = list()
    cur_time = 0

    while minheap:
        # pop every order and unless there are multiple serve times add to return list
        cur_pair = heapq.heappop(minheap)
        print(cur_pair)
        if cur_time != cur_pair[0]:
            # Empty the heap for ordered by customer order
            while minheap2:
                ret.append(heapq.heappop(minheap2) + 1)

            cur_time = cur_pair[0]
            heapq.heappush(minheap2, cur_pair[1])
        # orders with the same serve time are sorted then pushed using minheap2
        else:
            heapq.heappush(minheap2, cur_pair[1])

    while minheap2:
        ret.append(heapq.heappop(minheap2) + 1)

    return ret  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
