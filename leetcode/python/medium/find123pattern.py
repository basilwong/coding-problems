from collections import deque

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        if not nums or len(nums) < 3:
            return False

        store = deque()
        nums.append(nums[-1])
        end = -2
        mid = nums[end]
        for i in range(len(nums) - 2):
            store.append(nums[i] - mid)


        while len(store) >= 2:
            neg = False
            for x in store:
                x += (mid - nums[end + 1])
                if x < 0:
                    neg = True
                elif neg and x > 0:
                    return True
            end -= 1
            mid = nums[end]
            store.pop()

        return False
