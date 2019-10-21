                            ###Binary Tree Postorder Traversal###
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?

#Iterative Solution

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        output = []
        s1 = []                #stack 1
        s2 = []                #stack 2

        s1.append(root)
        while s1:
            root = s1.pop()
            s2.append(root)
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
        while s2:
            root = s2.pop()
            output.append(root.val)
        return output

root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(8)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
print Solution().postorderTraversal(root)
