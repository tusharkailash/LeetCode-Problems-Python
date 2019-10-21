                                ###Binary Tree Preorder Traversal###

# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

#Iterative Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        output = []

        if not root:
            return []

        s.append(root)

        while s:
            root = s.pop()
            output.append(root.val)

            if root.right:
                s.append(root.right)

            if root.left:
                s.append(root.left)

        return output



root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(8)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
print Solution().preorderTraversal(root)
