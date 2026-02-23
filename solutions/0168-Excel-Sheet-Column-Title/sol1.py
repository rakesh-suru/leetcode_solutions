class Solution:
    def binaryGap(self, n: int) -> int:
        temp = bin(n)[2:]
        ones = [i for i, val in enumerate(temp) if val == "1"]
        ans = 0
        for i in range(len(ones) - 1):
            ans = max(ans, ones[i + 1] - ones[i])
        return ans