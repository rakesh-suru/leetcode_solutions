# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        temp = head

        while temp:
            if temp not in seen:
                seen.add(temp)
            else:
                return temp
            
            temp = temp.next
        
        return None