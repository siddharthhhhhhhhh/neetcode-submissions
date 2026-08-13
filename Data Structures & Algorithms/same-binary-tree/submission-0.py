# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackp = [p]
        stackq = [q]
        while stackp:
            a = stackp.pop()
            b = stackq.pop()
            if a is None and b is None:
                continue
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            stackp.append(a.left)
            stackp.append(a.right)
            stackq.append(b.left)
            stackq.append(b.right)
            
            
        return True
        
