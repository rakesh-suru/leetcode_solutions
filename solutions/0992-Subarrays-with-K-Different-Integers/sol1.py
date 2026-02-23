class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                if len(s) == k:
                    ans += 1
        return ans