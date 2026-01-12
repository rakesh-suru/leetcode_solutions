class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums.pop() - 1
        y = nums.pop() - 1
        return x * y