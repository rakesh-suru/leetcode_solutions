# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        after = prev
        for _ in range(b - a + 2):
            after = after.next

        prev.next = list2

        tail = list2
        while tail.next:
            tail = tail.next

        tail.next = after

        return list1