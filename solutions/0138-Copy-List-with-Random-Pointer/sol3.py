"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head

        while temp:
            new = Node(temp.val)
            new.next = temp.next
            temp.next = new
            temp = temp.next.next
        
        temp = head
        while temp:
            copy = temp.next
            if temp.random:
                copy.random = temp.random.next
            else:
                copy.random = None
            temp = temp.next.next
        
        dummy = Node(-1)
        res = dummy
        temp = head

        while temp:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        
        return dummy.next
