from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        maximum = 0
        counter = 0
        store = set()
        queue = deque()

        for c in s:
            if c in store:
                maximum = max(maximum, counter)
                while queue:
                    temp = queue.popleft()
                    counter -= 1
                    store.remove(temp)
                    if temp == c:
                        store.add(c)
                        queue.append(c)
                        counter += 1
                        break
            else:
                counter += 1
                store.add(c)
                queue.append(c)

        return max(maximum, counter)
