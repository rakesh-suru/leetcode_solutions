class Solution:
    def smallestNumber(self, n: int) -> int:
        temp = bin(n)[2:]
        ones = "1" * len(temp)
        return int(ones, 2)
