# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        templ = head
        while templ:
            templ = templ.next
            length += 1
        temp = curr = head
        if length == 1:
            return None
        elif length == 2:
            if n == 1:
                temp.next = None
                return curr
            elif n == 2:
                temp = temp.next
                curr.next = None
                return temp
        elif length - n == 0:
            temp = temp.next
            curr.next = None
            return temp
        target = length - n
        count = 0
        while count < target:
            if target-count == 1:
                temp.next = temp.next.next
                count += 1
            else:
                temp = temp.next
                count += 1
        return curr

        
            

        