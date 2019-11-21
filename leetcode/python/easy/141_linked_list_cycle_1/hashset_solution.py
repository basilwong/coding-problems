# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        visited = set()


        while head.next != None:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next

        return False
