# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# https://www.youtube.com/watch?v=vjt5Y6-1KsQ

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        s1 = []
        s2 = []
        output =[]
        s1.append(root)
        while s1 or s2:
            while s1:
                level = []
                size = len(s1)
                for i in range(size):
                    root = s1.pop()
                    level.append(root.val)
                    if root.left:
                        s2.append(root.left)
                    if root.right:
                        s2.append(root.right)
                output.append(level)
            while s2:
                level = []
                size = len(s2)
                for i in range(size):
                    root = s2.pop()
                    level.append(root.val)
                    if root.right:
                        s1.append(root.right)
                    if root.left:
                        s1.append(root.left)
                output.append(level)
        return output

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print Solution().zigzagLevelOrder(root)
