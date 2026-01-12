# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        len1 = len2 = 0
        while temp1.next:
            len1 += 1
            temp1 = temp1.next
        while temp2.next:
            len2 += 1
            temp2 = temp2.next
        abs_len = abs(len1 - len2)

        temp1 = headA
        temp2 = headB

        for _ in range(abs_len):
            if len2 > len1:
                temp2 = temp2.next
            else:
                temp1 = temp1.next

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next
        
        return temp1
