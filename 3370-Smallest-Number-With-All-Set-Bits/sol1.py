class Solution:
    def smallestNumber(self, n: int) -> int:
        temp = 0
        while 2 ** temp <= n:
            temp += 1
        return 2 ** temp - 1