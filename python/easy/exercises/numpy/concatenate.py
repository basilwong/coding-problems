import numpy as np

"""
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
"""

measurements = np.array(input().strip().split( ), int)

N = measurements[0]
M = measurements[1]
P = measurements[2]

arrA = np.array([input().split() for _ in range(N)],int)
arrB = np.array([input().split() for _ in range(M)],int)
print(np.concatenate((arrA, arrB), axis = 0))