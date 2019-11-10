# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left):
            return True

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print Solution().isSymmetric(root)
