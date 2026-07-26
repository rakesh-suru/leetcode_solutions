# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_ptr = list1
        b_ptr = list1
        temp = list1

        for i in range(b + 1):
            if i < a - 1:
                a_ptr = a_ptr.next
            b_ptr = b_ptr.next
        
        a_ptr.next = list2
        end = list2

        while end.next:
            end = end.next
        
        end.next = b_ptr

        return list1