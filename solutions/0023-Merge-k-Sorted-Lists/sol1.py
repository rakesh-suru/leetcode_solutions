# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            temp = head
            while temp:
                values.append(temp.val)
                temp = temp.next
            
        values.sort()
        head = ListNode(-1)
        temp = head
        for num in values:
            new = ListNode(num)
            temp.next = new
            temp = temp.next
        
        return head.next