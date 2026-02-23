class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            odds = 0
            for j in range(i, len(nums)):
                if nums[j] % 2 == 1:
                    odds += 1
                if odds == k:
                    ans += 1
        return ans