# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)
#
# Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.
#
# The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
#
# The right-most node is also defined by the same way with left and right exchanged.
# Input:
#     ____1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10

# Ouput:
# [1,2,4,7,8,9,10,6,3]
#
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to definition)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        output = []
        output.append(root.val)
        self.left(root.left, output)
        self.leaves(root.left, output)
        self.leaves(root.right, output)
        self.right(root.right, output)
        return output

    def left(self, root, output):
        if not root or (not root.left and not root.right):
            return
        output.append(root.val)
        if root.left:
            self.left(root.left, output)
        else:
            self.left(root.right, output)

    def right(self, root, output):
        if not root or (not root.left and not root.right):
            return
        if root.right:
            self.right(root.right, output)
        else:
            self.right(root.left, output)
        output.append(root.val)

    def leaves(self, root, output):
        if not root:
            return
        if not root.left and not root.right:
            output.append(root.val)
        self.leaves(root.left, output)
        self.leaves(root.right, output)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)
print Solution().boundaryOfBinaryTree(root)