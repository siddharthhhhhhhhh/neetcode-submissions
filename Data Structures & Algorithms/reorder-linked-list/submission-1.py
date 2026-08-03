# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head:
            curr = head
                
            if curr.next:
                if curr.next.next == None:
                    return
                while curr.next.next:
                    curr = curr.next
                curr.next.next = head.next
                head.next = curr.next
                curr.next = None
                if head.next == None:
                    break
                else:
                    head = head.next.next      
                
                 
            else:
                return

            



        