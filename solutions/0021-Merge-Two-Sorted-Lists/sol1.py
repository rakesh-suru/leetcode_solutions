# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        temp1 = list1
        tail = None
        while temp1:
            values.append(temp1.val)
            tail = temp1
            temp1 = temp1.next
        
        temp2 = list2
        while temp2:
            values.append(temp2.val)
            temp2 = temp2.next

        values.sort()

        if tail:
            tail.next = list2
            temp = list1
        else:
            temp = list2

        head = temp
        i = 0
        while temp:
            temp.val = values[i]
            i += 1
            temp = temp.next
        
        return head