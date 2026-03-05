# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def solve(head):
            if not head or not head.next:
                return head
            
            newHead = solve(head.next)
            front = head.next
            front.next = head
            head.next = None

            return newHead
        
        return solve(head)