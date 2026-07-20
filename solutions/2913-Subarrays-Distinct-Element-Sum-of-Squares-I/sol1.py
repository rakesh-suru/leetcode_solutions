class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                temp = set(nums[i : j + 1])
                ans += len(temp) ** 2
        
        return ans