"""
Prints the sum of all the even numbers in the fibonacci sequence of length n.
"""


def only_even_sum(n):
    """
    Finds the sum of all the even fibonacci numbers under n.
    :param n: limiting number
    :return: sum
    """
    if (n < 2):
        return 0

    a = 0
    b = 2
    sum = 2

    while (b <= n):
        c = 4 * b + a
        if (c > n):
            break
        a = b
        b = c
        sum = sum + b

    return sum

# def find_fib(n):
#     """
#     Uses doubling to increase the speed of the fibonacci calculation.
#     :param n: fibonacci number to find
#     :return:
#     """
#     if n == 0:
#         return 0, 1
#     else:
#         a, b = find_fib(n // 2)
#         c = a * (b * 2 - a)
#         d = a * a + b * b
#         if n % 2 == 0:
#             return c, d
#         else:
#             return d, c + d

#
# def even_fib_sum(n):
#     """
#     Finds the sum of all the even fibonacci numbers under n.
#     :param n: limiting number
#     :return: sum
#     """
#     sum = 0
#     if n % 2 == 0:
#         for i in range(0, n, 2):
#             a, b = find_fib(i)
#             if a % 2 == 0:
#                 sum += a
#             if b % 2 == 0:
#                 sum += b
#     else:
#         for i in range(0, n, 2):
#             a, b = find_fib(i)
#             if a % 2 == 0:
#                 sum += a
#             if b % 2 == 0:
#                 sum += b
#     return sum


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(only_even_sum(n))
