from fractions import Fraction
from functools import reduce

"""
Given a list of rational numbers, finds their product.
"""


def product(fracs):
    # finds the product of the list of fractions and returns the numerator and denominator
    t = reduce(lambda x, y : x*y, fracs)
    return t.numerator, t.denominator




if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)