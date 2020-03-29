"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:

    def pre_order(self, left_sibling, right_sibling):
        if left_sibling:
            left_sibling.next = right_sibling
            self.pre_order(left_sibling.left, left_sibling.right)
            if right_sibling:
                self.pre_order(left_sibling.right, right_sibling.left)
            else:
                self.pre_order(left_sibling.right, None)
        if right_sibling:
            self.pre_order(right_sibling, None)

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        root.next = None

        self.pre_order(root.left, root.right)
        self.pre_order(root.right, None)

        return root
