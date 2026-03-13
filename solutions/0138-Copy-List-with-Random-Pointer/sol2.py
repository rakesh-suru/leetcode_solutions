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
        if not head:
            return None

        mapper = {}
        temp = head

        while temp:
            mapper[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            mapper[temp].next = mapper.get(temp.next)
            mapper[temp].random = mapper.get(temp.random)
            temp = temp.next

        return mapper[head]