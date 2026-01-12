class Solution:
    def minElement(self, nums: List[int]) -> int:
        minsum = float('inf')
        for num in nums:
            temp = num
            tempsum = 0
            while temp > 0:
                tempsum += temp % 10
                temp //= 10
            minsum = min(minsum, tempsum)
        return minsum
