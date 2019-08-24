import unittest
import random

def max_sub_array(arr):

    tracker_sum = 0
    max_sub_arr = -10000
    max_sub_seq = 0

    # Iterate through the array
    for num in arr:
        if num > 0:
            max_sub_seq += num
        if 0 > num + tracker_sum:
            tracker_sum = 0
        else:
            tracker_sum += num
        if tracker_sum > max_sub_arr:
            max_sub_arr = tracker_sum

    if not max_sub_seq > 0:
        max_sub_seq = max(arr)
    if not max_sub_arr > 0:
        max_sub_arr = max(arr)

    return [max_sub_arr, max_sub_seq]

class BasicTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max_sub_array([-1, -1, -1, -5, -6]), [-1, -1])

    def test_2(self):
        self.assertEqual(max_sub_array([5, -3, -3, -3, 5, -2, 1]), [5, 11])

if __name__ == '__main__':
    unittest.main()
