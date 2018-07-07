"""
This file contains two concepts. Generation of n fibonacci numbers and the use of the lambda and map functionals to cube
each fibonacci number.
"""

cube = lambda x: x*x*x

def gen_fibs(n):
    fib = []
    a = 0
    b = 1
    for i in range(n):
        fib.append(a)
        temp = a
        a = b
        b = b + temp
    return fib

if __name__ == '__main__':
    n = int(input())
    fib = list(map(cube, gen_fibs(n)))
    print(fib)
