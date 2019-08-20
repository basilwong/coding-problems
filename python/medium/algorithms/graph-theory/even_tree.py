import unittest
import math
import os
import random
import re
import sys

def dfs(graph, visited, val, cur):
    subtree_len = 0
    total = 0

    for node in graph[cur]:
        if node not in visited:
            visited.add(node)
            subtree_len = dfs(graph, visited, val, node)

            if subtree_len % 2 == 0:
                # In this case the subtree is even so remove the branch
                val[0] += 1
            else:
                # Add the odd subtree length to the total
                total += subtree_len

    return total + 1

def evenForest(t_nodes, t_edges, t_from, t_to):

    graph = [set() for i in range(t_nodes)]

    # Traverse Tree in revserse
    for i in range(t_edges):
        graph[t_to[i] - 1].add(t_from[i] - 1)

    # Depth First Search
    val = [0]
    visited = set()
    dfs(graph, visited, val, 0)
    return val[0]

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        fr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
        self.assertEqual(evenForest(10, 9, fr, to), 2)

# if __name__ == '__main__':
#     unittest.main()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
