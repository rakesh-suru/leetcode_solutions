class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cur = 1
        for i in range(1, k+1):
            if cur % k == 0:
                return i
            cur = 10 * (cur % k) + 1
        
        return -1