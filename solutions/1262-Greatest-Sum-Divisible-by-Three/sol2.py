class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -float('inf'), -float('inf')]
        
        for n in nums:
            new = dp[:]  # clone
            for r in range(3):
                nr = (r + n) % 3
                new[nr] = max(new[nr], dp[r] + n)
            dp = new
        
        return dp[0]
