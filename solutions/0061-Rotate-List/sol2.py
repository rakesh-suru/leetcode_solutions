# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        cnt = 1
        
        while temp.next:
            cnt += 1
            temp = temp.next
        
        k %= cnt
        move = cnt - k

        new = head
        temp.next = head
        for _ in range(move - 1):
            new = new.next
        
        head = new.next
        new.next = None

        return head