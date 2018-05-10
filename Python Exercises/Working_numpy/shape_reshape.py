# reshaping colunm vetor to 3x3 matrix

import numpy

arr = numpy.array(input().strip().split(' '), float)
print(numpy.reshape(arr, (3,3)))