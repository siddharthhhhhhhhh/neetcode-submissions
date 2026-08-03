# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        count1 = 0
        res1 = 0
        while curr1:
            res1 += (curr1.val) * (10**count1)
            count1 += 1
            curr1 = curr1.next
        curr2 = l2
        count2 = 0
        res2 = 0
        while curr2:
            res2 += (curr2.val) * (10**count2)
            count2 += 1
            curr2 = curr2.next
        
        res3 = res1 + res2
        res4 = str(res3)
        final = copy = ListNode()
        if len(res4) == 1:
            final = ListNode(res4[0])
            return final
        else:
            for i in range(len(res4)):
                copy1 = ListNode(res4[len(res4)-i-1])
                copy.next = copy1
                copy = copy.next
        return final.next
                

       
            