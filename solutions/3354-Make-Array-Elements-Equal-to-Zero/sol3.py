class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                left_sum = sum(nums[:i])
                right_sum = sum(nums[i+1:])
                if 0 <= left_sum - right_sum <= 1:
                    ans += 1
                if 0 <= right_sum - left_sum <= 1:
                    ans += 1
        return ans
