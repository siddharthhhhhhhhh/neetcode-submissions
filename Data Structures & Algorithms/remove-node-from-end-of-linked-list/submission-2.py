# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next
        if len(list1) == 1:
            if n == 1:
                head = None
                return head
        if (len(list1)-n) == 0:
            head = head.next
            return head
        
        count = 0
        curr = head
        while curr:
            
            if curr.next:
                if count+1 != (len(list1)-n):
                    curr = curr.next
                elif count+1 == (len(list1)-n):
                    if curr.next.next:
                        curr.next = curr.next.next
                        curr = curr.next
                    elif curr.next.next == None:
                        curr.next = None
                        curr = curr.next
                count = count + 1
            else:
                curr = None
        return head
            

        