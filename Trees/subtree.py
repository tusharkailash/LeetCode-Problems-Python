                            ###Subtree of Another Tree###

# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
# Example 1:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None:
            return True
        if s is None:
            return False
        if self.identical(s,t):
            return True
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

    def identical(self,s,t):
        if not s and not t:
            return True
        if s is not None and t is not None:
            if(s.val == t.val and self.identical(s.left,t.left) and self.identical(s.right,t.right)):
                return True
            else:
                return False

s = TreeNode(3)
s.left = TreeNode(4)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.right = TreeNode(5)


t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
print Solution().isSubtree(s,t)
