class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        total = prefix[-1]
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                left = prefix[i]
                right = total - prefix[i]
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
        return ans
