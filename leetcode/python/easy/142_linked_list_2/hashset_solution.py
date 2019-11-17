# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head:
            return None

        while head.next:

            head.val = str(head.val)

            head = head.next

            if type(head.val) is str:
                head.val = int(head.val)
                return head

        return None
