import numpy as np

"""
1 4
1 2 3 4
5 6 7 8
"""

n, m = map(int, input().split())
A, B = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))

print(np.add(A,B), np.subtract(A,B), np.multiply(A,B,), np.floor_divide(A,B), np.mod(A,B), np.power(A,B), sep = "\n")