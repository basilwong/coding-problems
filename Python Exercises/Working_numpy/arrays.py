import numpy

# Reverses the order of the array elements and casts them to float.
def arrays(arr):
   return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)