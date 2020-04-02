import random

class Solution:

    def partition(self, nums, left, right):

        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]

        frontier = left
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[i], nums[frontier] = nums[frontier], nums[i]
                frontier += 1

        nums[frontier], nums[right] = nums[right], nums[frontier]
        return frontier

    def quick_select(self, nums, left, right, k):

        pivot = self.partition(nums, left, right)
        if pivot == k:
            return nums[k]
        elif pivot < k:
            return self.quick_select(nums, pivot + 1, right, k)
        else:
            return self.quick_select(nums, left, pivot - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return nums[0]

        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
