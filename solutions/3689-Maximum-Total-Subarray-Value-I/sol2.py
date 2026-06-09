class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxi = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                temp = nums[i : j + 1]
                maxi = max(maxi, max(temp) - min(temp))
        
        return maxi * k