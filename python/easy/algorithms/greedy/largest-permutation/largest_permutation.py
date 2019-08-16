import unittest
import random

def largest_permutation(n, arr):

    # import pdb; pdb.set_trace()
    nums = len(arr)
    pos = [-1] * nums

    for i in range(nums):
        pos[arr[i] - 1] = i

    index = 0
    while index < n and index < nums:
        if arr[index] == nums - index:
            n += 1
            index += 1
        else:
            temp = arr[index] - 1
            arr[pos[nums - index - 1]], arr[index] = arr[index], arr[pos[nums - index - 1]]
            pos[temp] = pos[arr[index] - 1]
            index += 1

    return arr

class BasicTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(largest_permutation(1, [4, 2, 3, 5, 1]), [5, 2, 3, 4, 1])

    def test_2(self):
        self.assertEqual(largest_permutation(1, [2, 1, 3]), [3, 1, 2])

    def test_3(self):
        self.assertEqual(largest_permutation(1, [2, 1]), [2, 1])

    def test_switches(self):
        arr1 = [9, 8, 1, 4, 2, 5, 7, 6, 3, 10]
        arr2 = [10, 9, 1, 4, 2, 5, 7, 6, 3, 8]
        arr1_res = [10, 9, 1, 4, 2, 5, 7, 6, 3, 8]
        arr2_res = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]
        self.assertEqual(largest_permutation(2, arr1), arr1_res)
        self.assertEqual(largest_permutation(3, arr2), arr2_res)

    def test_full_switch(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(largest_permutation(5, arr), [5, 4, 3, 2, 1])

    def test_3(self):
# 9785 8076
        # Get input
        text_input = open("input01.txt", 'r')
        lines = text_input.readlines()
        text_input.close()

        del lines[0]
        input = list(map(int, lines[0].split(' ')))


        # Get output
        text_output = open("output01.txt", 'r')
        out_str = text_output.readline().strip('\n').split(' ')
        text_output.close()

        a_output = list(map(int, out_str))

        #Check
        self.maxDiff = 10
        self.assertEqual(largest_permutation(8076, input), a_output)

if __name__ == '__main__':
    unittest.main()
