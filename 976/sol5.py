class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[j] + nums[k] > nums[i]:
                        ans = max(ans, nums[i] + nums[j] + nums[k])
                        break
        return ans
