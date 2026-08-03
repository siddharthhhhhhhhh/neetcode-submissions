# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1 = [root.val]
        
        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            if left:
                list1.append(root.left.val)
            right = dfs(root.right)
            if right:
                list1.append(root.right.val)
            return True
        dfs(root)
        list1.sort()
        return list1[k-1]
            

        