class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        ans = min(ans, dist)
        
        return ans if ans != float("inf") else -1