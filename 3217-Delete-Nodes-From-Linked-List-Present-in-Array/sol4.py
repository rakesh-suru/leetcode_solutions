# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        if not head:
            return None
        if head.val in nums:
            return self.modifiedList(nums, head.next)
        head.next = self.modifiedList(nums, head.next)
        return head
