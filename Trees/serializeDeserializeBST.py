# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = []
        self.postorder(root,output)
        return ' '.join(map(str,output))

    def postorder(self, root, output):
        if not root:
            return
        self.postorder(root.left, output)
        self.postorder(root.right, output)
        output.append(root.val)
        return output


    def deserialize(self, data):

        low = float("-inf")
        high = float("inf")

        def helper(low,high):
            if not data or data[-1] < low or data[-1] > high:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, high)
            root.left = helper(low, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper(low,high)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root = TreeNode(10)
root.left = TreeNode(10)
root.left.left = TreeNode(-5)
root.right = TreeNode(19)
root.right.left = TreeNode(17)
root.right.right = TreeNode(21)
a = Codec().serialize(root)
print Codec().deserialize(a)