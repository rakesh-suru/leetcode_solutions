class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        same = [0] * n
        diff = [0] * n
        
        same[0] = 6
        diff[0] = 6
        
        for i in range(1, n):
            same[i] = (same[i-1] * 3 + diff[i-1] * 2) % MOD
            diff[i] = (same[i-1] * 2 + diff[i-1] * 2) % MOD
        
        return (same[n-1] + diff[n-1]) % MOD
