class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return
        root = TreeNode(postorder[-1])
        for i in range(len(inorder)-1,-1,-1):
            if postorder[-1] == inorder[i]:
                root.left = self.buildTree(inorder[:i], postorder[:i])
                root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
                return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print Solution().buildTree(inorder,postorder)