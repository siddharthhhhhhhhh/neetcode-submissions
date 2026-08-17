# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1 = []
        self.dfs(root, list1)
        heapq.heapify(list1)
        for i in range(k):
            x = heapq.heappop(list1)
        return x
    def dfs(self, root, list1):
        if root is None:
            return
        list1.append(root.val)
        left = self.dfs(root.left, list1)
        right = self.dfs(root.right, list1)
        return


        