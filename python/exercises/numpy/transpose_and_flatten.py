import numpy

# prints the transpose and flattened version of the input array
"""
2 2
1 2
3 4
"""
arr = list()

arr1 = input().strip().split(' ')
N = int(arr1[0])

for i in range(N):
    arr.append(input().strip().split(' '))

arr_np = numpy.array(arr, int)
print(arr_np.transpose())
print(arr_np.flatten())