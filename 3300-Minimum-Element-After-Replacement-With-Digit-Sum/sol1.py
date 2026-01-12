class Solution:
    def minElement(self, nums: List[int]) -> int:
        minsum = 99
        for num in nums:
            temp = num
            tempsum = 0
            while temp > 0:
                r = temp % 10
                tempsum += r
                temp = temp // 10
            minsum = min(minsum, tempsum)
        return minsum
