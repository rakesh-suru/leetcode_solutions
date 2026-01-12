# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = prev = head
        temp = temp.next

        while temp:
            new = ListNode(math.gcd(prev.val, temp.val))
            prev.next = new
            new.next = temp

            prev = temp
            temp = temp.next
        
        return head