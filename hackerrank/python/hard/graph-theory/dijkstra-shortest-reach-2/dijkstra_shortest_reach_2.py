#!/bin/python3
import unittest
import math
import os
import random
import re
import sys
import collections


# Solution for unoptimized input
def convert_to_graph(n, edges):
    graph = [set() for _ in range(n)]
    for e in edges:
        graph[e[0] - 1].add((e[1] - 1, e[2]))
        graph[e[1] - 1].add((e[0] - 1, e[2]))

    return graph


def shortestReach(n, edges, s):

    graph = convert_to_graph
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

# Solution for optimized input
def main_optimized_input():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = [set() for _ in range(n)]

        for _ in range(m):
            e = list(map(int, input().rstrip().split()))
            edges[e[0] - 1].add((e[1] - 1, e[2]))
            edges[e[1] - 1].add((e[0] - 1, e[2]))

        s = int(input())

        result = shortestReach_2(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


def shortestReach_2(n, graph, s):

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

    def test_3(self):

        # Get input
        text_input = open("input07.txt", 'r')
        lines = text_input.readlines()
        text_input.close()
        del lines[0]
        for l in lines:
            l.strip('\n')

        start = int(lines.pop())
        n = lines[0].split(' ')

        del lines[0]
        # graph
        graph = [list(map(int, x.split(' '))) for x in lines]

        # Get output
        text_output = open("output07.txt", 'r')
        out_str = text_output.readline().strip('\n').split(' ')
        text_output.close()

        a_output = list(map(int, out_str))
        #Check
        self.assertEqual(shortestReach(int(n[0]), graph, start), a_output)





if __name__ == '__main__':
    unittest.main()
