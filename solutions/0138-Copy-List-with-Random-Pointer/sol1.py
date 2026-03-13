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
        mapper = {}
        temp = head

        while temp:
            new = Node(temp.val)
            mapper[temp] = new
            temp = temp.next
        
        temp = head
        newHead = Node(-1)
        copy = newHead

        while temp:
            node = mapper[temp]

            node.next = mapper.get(temp.next)
            node.random = mapper.get(temp.random)

            copy.next = node
            copy = copy.next

            temp = temp.next
        
        return newHead.next