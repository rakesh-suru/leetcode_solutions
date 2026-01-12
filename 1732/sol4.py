class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        dp = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            dp[i+1] = dp[i] + gain[i]
        return max(dp)
