# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        maxr = root.val
        return (1 + self.isGnode(root.left, maxr) + self.isGnode(root.right, maxr))

    def isGnode(self, root, maxr):
        if root == None:
            return 0
        if root.val >= maxr:
            count = 1
        else:
            count = 0
        maxt = max(root.val, maxr)
        return count + self.isGnode(root.left, maxt) + self.isGnode(root.right, maxt)
