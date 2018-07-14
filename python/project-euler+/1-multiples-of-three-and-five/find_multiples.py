"""
Outputs the sum of the numbers that are multiples under 3 and 5.

Example Test Case:
12
10
100
1000
10000
100000
1000000
10000000
100000000
1000000000
10000000000
100000000000
1000000000000
"""

import datetime
import math

def sum_equations(n):
    """
    Uses sum equations to find the sum of multiples of 3 and 5 less than n.
    :param n: limiting number
    :return: sum
    """
    multiple_3_n = n // 3
    multiple_5_n = n // 5
    multiple_15_n = n // 15
    if (multiple_15_n * 15 == n):
        multiple_15_n -= 1
    if (multiple_5_n * 5 == n):
        multiple_5_n -= 1
    if (multiple_3_n * 3 == n):
        multiple_3_n -= 1
    sum_3 = multiple_3_n * (3 + 3 * multiple_3_n) // 2
    sum_5 = multiple_5_n * (10 + (multiple_5_n - 1) * 5) // 2
    sum_15 = multiple_15_n * (30 + (multiple_15_n - 1) * 15) // 2
    return int(sum_3 + sum_5 - sum_15 )


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(sum_equations(n))





    # for _ in range(t):
    #     n = int(input().strip())
    #     # Comparing the time for each of the functions.
    #
    #     # Individual Adding
    #     a = datetime.datetime.now()
    #     print(individual_adding(n))
    #     b = datetime.datetime.now()
    #     c = b - a
    #
    #     # Sum equations
    #     a = datetime.datetime.now()
    #     print(sum_equations(n))
    #     b = datetime.datetime.now()
    #     d = b - a
    #
    #     print('\n\n Time for individual sums:')
    #     print(c.microseconds)
    #     print('\n Time for sum equations:')
    #     print(d.microseconds)

