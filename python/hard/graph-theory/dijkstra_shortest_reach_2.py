#!/bin/python3
import unittest
import math
import os
import random
import re
import sys
import collections

# Complete the shortestReach function below.
def shortestReach(n, edges, s):

    graph = [set() for _ in range(n)]
    for e in edges:
        graph[e[0] - 1].add((e[1] - 1, e[2]))
        graph[e[1] - 1].add((e[0] - 1, e[2]))

    lengths = [-1] * n
    lengths[s - 1] = 0

    queue = collections.deque()
    queue.append(s - 1)

    while queue:
        cur = queue.popleft()
        for tup in graph[cur]:
            if lengths[tup[0]] == -1:
                lengths[tup[0]] = lengths[cur] + tup[1]
                queue.append(tup[0])
            elif lengths[tup[0]] >= lengths[cur] + tup[1]:
                lengths[tup[0]] = lengths[cur] + tup[1]
                queue.append(tup[0])

    del lengths[s - 1]
    return lengths


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        graph = [[1, 2, 10], [1, 3, 6], [2, 4, 8]]
        out = [10, 16, 8, -1]
        self.assertEqual(shortestReach(5, graph, 2), out)

    def test_2(self):
        graph = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]
        out = [24, 3, 15]
        self.assertEqual(shortestReach(4, graph, 1), out)

if __name__ == '__main__':
    unittest.main()
