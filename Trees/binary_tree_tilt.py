                    ### Binary Tree Tilt

#
# Given a binary tree, return the tilt of the whole tree.
#
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
#
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
#
# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global ans  # as we are accessing this value in the other function.
        ans = 0
        self.getvalue(root)
        return ans

    def getvalue(self, root):
        if not root:
            return 0
        left = self.getvalue(root.left)
        right = self.getvalue(root.right)
        global ans  # as we are accessing this value in the other function.
        ans += abs(left - right)  # we need to return the difference between two nodes value for evry node.

        return root.val + left + right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print Solution().findTilt(root)