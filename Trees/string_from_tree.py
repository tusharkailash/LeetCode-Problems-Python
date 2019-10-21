# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        if t.left is None and t.right is None:
            return str(t.val)
        if t.right is None:
            return str(t .val) +"("+ self.tree2str(t.left)+")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.left.left.left = TreeNode(6)
t.right = TreeNode(3)
print Solution().tree2str(t)
