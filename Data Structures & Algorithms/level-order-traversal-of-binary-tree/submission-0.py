# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        list1 = []
        stack = deque([root])
        while stack:
            level = len(stack)
            list2 = []
            for i in range(level):
                x = stack.popleft()
                list2.append(x.val)
                if x.left:
                    stack.append(x.left)
                if x.right:
                    stack.append(x.right)
            list1.append(list2)
        return list1
