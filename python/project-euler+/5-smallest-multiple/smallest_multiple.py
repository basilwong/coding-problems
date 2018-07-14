"""
Calculates what the smallest multiple from 1 to N is.
"""

from operator import mul
import numpy as np
from functools import reduce
from math import sqrt
from itertools import count, islice


def is_prime(x):
    """
    Returns true if the number is a prime number.
    :param x: the number in question
    :return: boolean of whether the number is prime
    """
    return x > 1 and all(x % i for i in islice(count(2), int(sqrt(x)-1)))


def find_prime_nums(n):
    """
    Finds all the prime numbers that are less than or equal to n.
    :param n: limiting number
    :return: a list of all the prime numbers
    """
    prime_list = list()
    if n < 2:
        return prime_list
    for i in islice(count(2), n - 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def find_largest_exponent(p, n):
    """
    Finds the largest number k such that p^k < m.
    :param p: parameter that the exponent affects
    :param m: limiting number
    :return: k, the largest possible exponent
    """
    k = 2
    while p**k <= n:
        k += 1
    return k - 1

def smallest_multiple_dir(n):
    """
    M is divisible by all numbers from 1 to n if and only if M is equal to the product of all prime powers p^k where p
    is prime and divides M, and p < n, and k is the largest integer such that p^k < n.
    For example, 2520 = 2^3 * 3^2 * 5 * 7
    :param n: limiting number of multiples
    :return: the smallest multiple of all the numbers less than or equal to n
    """
    if n < 2:
        if n == 1:
            return 1
        else:
            return 0
    primes = find_prime_nums(n)

    for index in range(len(primes)):
        primes[index] = primes[index]**find_largest_exponent(primes[index], n)

    return reduce(mul, primes)



def smallest_multiple_iter(n):
    """
    Finds the smallest multiple of all the numbers smaller than or equal to n checking all the mutiples of the largest
    number.
    :param n: limiting number
    :return: smallest multiple
    """
    a = range(1, n+1)
    a = np.array(a)
    prod = reduce(mul, a)
    ch = prod
    while (ch >= n):
        is_multiple = True
        for i in a:
            if ch % i != 0:
                is_multiple = False
        if is_multiple:
            prod = ch
        ch -= n
    return prod


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(smallest_multiple_dir(n))