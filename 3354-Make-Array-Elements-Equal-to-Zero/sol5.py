class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left = ans = 0
        for num in nums:
            right = total - left
            if num == 0:
                ans += (0 <= left - right <= 1) + (0 <= right - left <= 1)
            else:
                left += num
        return ans
