# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        list1 = [[root.val]]
        stack = deque([root])
        while stack:
            list2 = []
            count2 = 0
            for i in range(len(stack)):
                node = stack.popleft()
                if node != None:
                    if node.left != None:
                        stack.append(node.left)
                        list2.append(node.left.val)
                        count2 += 1
                    if node.right != None:
                        stack.append(node.right)
                        list2.append(node.right.val)
                        count2 += 1
            if count2 > 0:
                list1.append(list2)
                count2 = 0
        return list1


