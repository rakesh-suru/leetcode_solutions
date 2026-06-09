class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxi, mini = 0, float("inf")

        for num in nums:
            if num > maxi:
                maxi = num
            if num < mini:
                mini = num
        
        return (maxi - mini) * k