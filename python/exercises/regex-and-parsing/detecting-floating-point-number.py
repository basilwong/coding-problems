"""
Verifies that the given strings can be converted into float numbers.

Note: A quicker way would have been to use REGEX:
import re
for _ in range(int(input())):
	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
"""


def check_float(s):
    try:
        float(s)
    except(Exception):
        return False
    else:
        if (s == '0'):
            return False
        return True

if __name__ == '__main__':
    t = int(input())
    inputs = list()
    for i in range(t):
        inputs.append(input())

    for inp in inputs:
        if (check_float(inp)):
            print("True")
        else:
            print("False")

