# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr1 = curr2 = top = head
        while curr1.next:
            if curr1.next.next:
                while curr2.next.next:
                    curr2 = curr2.next
                curr2.next.next = curr1.next
                curr1.next = curr2.next
                curr2.next = None
                curr1 = curr2 = curr1.next.next
            else: 
                break
      
                
        