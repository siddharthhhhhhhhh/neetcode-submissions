# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left == -1 or right == -1:
            return -1
        if left>=right:
            if left - right > 1:
                return -1
            else: 
                return 1 + max(left, right)
        else:
            if right - left > 1:
                return -1
            else:
                return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = self.height(root)
        if diff == -1:
            return False
        else: 
            return True
    
    
        