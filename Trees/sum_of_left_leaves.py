                        ###Sum of left leaves###
#    3
#   / \
#  9  20
#    /  \
#   15   7
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root:
            l = root.left
            r = root.right
            if l and (l.left or l.right) is None:
                ans += l.val
            ans += self.sumOfLeftLeaves(l) + self.sumOfLeftLeaves(r)
        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print Solution().sumOfLeftLeaves(root)
