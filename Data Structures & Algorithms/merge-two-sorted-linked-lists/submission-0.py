# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 != None:
            return list2
        elif list2 == None and list1 != None:
            return list1
        elif list1 == None and list2 == None:
            return None
        if list1.val <= list2.val:
            temp1 = list1
            temp2 = list2
        else:
            temp1 = list2
            temp2 = list1
        root = temp1
        tempf = temp1.next
     
        while temp2 and tempf:
            if temp2.val <= tempf.val:
                temp1.next = temp2
                temp1 = temp1.next
                if temp2.next != None:
                    temp2 = temp2.next
                else:
                    temp2 = None
            else:
                temp1.next = tempf
                temp1 = temp1.next
                if tempf.next != None:
                    tempf = tempf.next
                else:
                    tempf = None
        if temp2 == None and tempf != None:
            temp1.next = tempf
        elif temp2 != None and tempf == None:
            temp1.next = temp2
        return root

    



        
        
        