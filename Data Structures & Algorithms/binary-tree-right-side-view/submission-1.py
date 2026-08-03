# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        list1 = [root.val]
        stack = deque([root])
        while stack:
            count = 0
            list2 = []
            
            
            for i in range(len(stack)):
                node = stack.popleft()
                if node != None:
                    if node.left != None:
                        list2.append(node.left.val)
                        stack.append(node.left)
                        count += 1
                    if node.right != None:
                        list2.append(node.right.val)
                        stack.append(node.right)
                        count += 1
            if count > 0:
                list1.append(list2[-1])
                count = 0
        return list1
                    

        
        