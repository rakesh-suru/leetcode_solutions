class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float("inf")

        for i in range(n):
            temp = nums[i:] + nums[:i]
            curr = 0
            for j in range(n):
                curr += temp[j] * j
            ans = max(ans, curr)
        
        return ans