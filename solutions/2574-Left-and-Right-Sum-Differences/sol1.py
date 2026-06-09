class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = nums[:]
        rightsum = nums[:]
        ans = nums[:]

        for i in range(1, n):
            leftsum[i] = nums[i] + leftsum[i - 1]
        
        for j in range(n - 2, -1, -1):
            rightsum[j] = nums[j] + rightsum[j + 1]

        for i in range(n):
            ans[i] = abs(leftsum[i] - rightsum[i])
        
        return ans