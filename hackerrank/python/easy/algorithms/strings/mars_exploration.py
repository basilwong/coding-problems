import unittest
import math
import os
import random
import re
import sys

"""
Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the
signal received by Earth as a string, , determine how many letters of the SOS message have been changed by
radiation.

Ex:

SOSSOS
- Return 0

OOSSOS
- Return 1

SOSOSS
-Return 2

"""
def marsExploration(s):
    state = 0
    counter = 0
    for ch in s:
        if state == 0:
            state = 1
            if ch != 'S':
                counter += 1
        elif state == 1:
            state = 2
            if ch != 'O':
                counter += 1
        elif state == 2:
            state = 0
            if ch != 'S':
                counter += 1
        else:
            print("Impossible State")

    return counter

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(marsExploration('SOSSPSSQSSOR'), 3)

    def test_2(self):
        self.assertEqual(marsExploration('SOSSOT'), 1)

    def test_3(self):
        self.assertEqual(marsExploration('SOSSOSSOS'), 0)


if __name__ == '__main__':
    unittest.main()
