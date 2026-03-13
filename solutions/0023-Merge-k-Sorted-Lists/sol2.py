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
                values.append(temp)
                temp = temp.next
            
        values.sort(key = lambda x : x.val)
        head = ListNode(-1)
        temp = head
        for node in values:
            temp.next = node
            temp = temp.next
        
        return head.next