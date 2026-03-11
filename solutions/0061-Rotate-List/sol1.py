# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        k %= cnt
        
        for _ in range(k):
            last = head
            prev = None

            while last.next:
                prev = last
                last = last.next

            last.next = head
            prev.next = None
            head = last
        
        return head