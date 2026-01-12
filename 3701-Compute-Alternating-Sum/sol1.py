class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = sum(nums[i] for i in range(0,len(nums),2))
        odd = sum(nums[i] for i in range(1, len(nums),2))
        return even - odd