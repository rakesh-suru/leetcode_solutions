# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0

        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        temp1 = head
        temp2 = prev

        while temp1 and temp2:
            ans = max(temp1.val + temp2.val, ans)
            temp1 = temp1.next
            temp2 = temp2.next
        
        return ans