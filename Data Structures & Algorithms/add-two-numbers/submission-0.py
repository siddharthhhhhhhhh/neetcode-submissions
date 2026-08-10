# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        temp1 = l1
        while temp1:
            list1.append(temp1.val)
            temp1 = temp1.next
        n1 = 0
        for i in range(len(list1)):
            n1 += (10**i)*list1[i]
        list2 = []
        temp2 = l2
        while temp2:
            list2.append(temp2.val)
            temp2 = temp2.next
        n2 = 0
        for i in range(len(list2)):
            n2 += (10**i)*list2[i]
        n3 = n1 + n2
        strn3 = str(n3)
        list3 = []
        for i in range(len(strn3)):
            list3.append(strn3[i])
        list3 = list3[::-1]
        curr = ListNode()
        for i in range(len(list3)):
            if i == 0:
                curr.val = list3[i]
                temp = curr
            else:
                temp.next = ListNode()
                temp.next.val = list3[i]
                temp = temp.next
        return curr