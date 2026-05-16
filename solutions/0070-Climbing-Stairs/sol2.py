class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        val1 = 2
        val2 = 3
        temp = 0

        for i in range(3,n):
            temp = val1+val2
            val1 = val2
            val2 = temp

        return temp