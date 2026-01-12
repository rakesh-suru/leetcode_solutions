class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num > 0  and (not stack or stack[-1] != num):
                stack.append(num)
                ans += 1
        return ans
