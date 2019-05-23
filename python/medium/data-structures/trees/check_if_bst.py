""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
  if root.left != None:
    if root.left.data >= root.data or not check_branch(root.left, root.data, -1):
      return False
  if root.right != None:
    if root.right.data <= root.data or not check_branch(root.right, 10001, root.data):
      return False
  return True

def check_branch(root, ma, mi):
  if root.left != None:
    if root.left.data >= root.data or root.left.data <= mi:
      return False
    if not check_branch(root.left, root.data, mi):
        return False
  if root.right != None:
    if root.right.data <= root.data or root.right.data >= ma:
      return False
    if not check_branch(root.right, ma, root.data):
        return False
  return True
