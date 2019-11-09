# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

max = float("inf")
min = float("-inf")

class Solution(object):
    def isValidBST(self, root):
        return self.IsBST(root, min, max)

    def IsBST(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val > max:
            return False
        return (self.IsBST(root.left, min, root.val) and self.IsBST(root.right, root.val, max))


root = TreeNode(10)
root.left = TreeNode(10)
root.left.left = TreeNode(-5)
root.right = TreeNode(19)
root.right.left = TreeNode(17)
root.right.right = TreeNode(21)
print Solution().isValidBST(root)

# https://www.youtube.com/watch?v=MILxfAbIhrE&t=371s
