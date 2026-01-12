class Solution:
    def smallestNumber(self, n: int) -> int:
        temp = bin(n)[2:]
        temp = temp.replace("0", "1")
        return int(temp, 2)
