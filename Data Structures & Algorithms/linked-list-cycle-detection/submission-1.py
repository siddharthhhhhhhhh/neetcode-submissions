# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list1 = []
        curr = head
        while curr:
            if curr.val not in list1:
                list1.append(curr.val)
                curr = curr.next
            elif curr.val in list1:
                if curr.next == None:
                    return False
                return True
        return False  
        