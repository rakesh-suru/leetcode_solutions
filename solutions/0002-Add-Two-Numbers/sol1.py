# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp1 = l1
        temp2 = l2

        curr = ListNode(-1)
        head = curr

        while temp1 and temp2:
            temp = temp1.val + temp2.val + carry
            if temp > 9:
                carry = 1
                temp -= 10
            else:
                carry = 0

            new = ListNode(temp)
            curr.next = new
            curr = new

            temp1 = temp1.next
            temp2 = temp2.next
        
        while temp1:
            temp = temp1.val + carry
            if temp > 9:
                carry = 1
                temp -= 10
            else:
                carry = 0

            new = ListNode(temp)
            curr.next = new
            curr = new

            temp1 = temp1.next
        
        while temp2:
            temp = temp2.val + carry
            if temp > 9:
                carry = 1
                temp -= 10
            else:
                carry = 0
                
            new = ListNode(temp)
            curr.next = new
            curr = new

            temp2 = temp2.next

        if carry:
            new = ListNode(carry)
            curr.next = new
            curr = new

        head = head.next

        return head