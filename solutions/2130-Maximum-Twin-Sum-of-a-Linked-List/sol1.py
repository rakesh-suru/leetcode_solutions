# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sums = []
        temp = head

        while temp:
            sums.append(temp.val)
            temp = temp.next
        
        n = len(sums)
        ans = 0
        for i in range(n//2 + 1):
            ans = max(ans, sums[i] + sums[n - i - 1])
        
        return ans