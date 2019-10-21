                      ###Binary Tree Inorder Traversal###
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

#Iteretive solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        output = []
        stack  = []

        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                if stack == []:
                    break
                else:
                    root = stack.pop()
                    output.append(root.val)
                    root = root.right
        return output


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
print Solution().inorderTraversal(root)
