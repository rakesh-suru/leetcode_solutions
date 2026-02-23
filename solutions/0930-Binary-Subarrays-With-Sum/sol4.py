class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        freq = {0: 1}
        prefixSum = 0

        for num in nums:
            prefixSum += num
            ans += freq.get(prefixSum - goal, 0)
            freq[prefixSum] = freq.get(prefixSum, 0) + 1

        return ans
