class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def solve(idx, remaining):
            if remaining == 0:
                return 1
            
            if idx >= n:
                return 0
            
            ans = 0

            ans += solve(idx + 1, remaining)
            
            for j in range(idx + 1, n):
                ans += solve(j, remaining - 1)
            
            return ans % MOD
        
        return solve(0, k) % MOD