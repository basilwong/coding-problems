# Given an integer n, return the number of trailing zeroes in n!.

import unittest

def trailingZeroes(n):
    divider = 5
    zeros = 0
    while n >= divider:
        zeros += int(n / divider)
        divider *= 5
    return zeros

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(trailingZeroes(10), 2)
        self.assertEqual(trailingZeroes(9), 1)
        self.assertEqual(trailingZeroes(11), 2)
        self.assertEqual(trailingZeroes(29), 6)
        self.assertEqual(trailingZeroes(3), 0)
        self.assertEqual(trailingZeroes(25), 6)


if __name__ == '__main__':
    unittest.main()
