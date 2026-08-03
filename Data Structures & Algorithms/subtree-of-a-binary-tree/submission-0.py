# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isPresent(root):
            stack = [(root, subRoot)]

            while stack:
                p, q = stack.pop()
                if not p and not q:
                    continue
                if not p or not q or p.val != q.val:
                    return False
                stack.append([p.left, q.left])
                stack.append([p.right, q.right])
            return True
        stack = [root]
        while stack:
            a = stack.pop()
            if not a:
                continue
            if a.val == subRoot.val:
                if isPresent(a):
                    return True
            stack.append(a.right)
            stack.append(a.left)
        
        return False