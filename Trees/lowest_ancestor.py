            ###Lowest Common Ancestor of a Binary Search Tree###

#        _______6______
#       /              \
#    ___2__          ___8__
#   /      \        /      \
#   0      _4       7       9
#         /  \
#         3   5
#For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return None
        if (root.val > max(p,q)):
            return self.lowestCommonAncestor(root.left,p,q)
        elif (root.val < min(p,q)):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root.val


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
print Solution().lowestCommonAncestor(root,2,4)
