class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        n = ""

        while num > 0:
            temp = min(sum, 9)
            n += str(temp)
            sum -= temp
            num -= 1
        
        if sum > 0:
            return ""
        return n