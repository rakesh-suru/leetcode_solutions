# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)
            new = ListNode(gcd_val)
            new.next = curr.next
            curr.next = new
            curr = new.next
        
        return head