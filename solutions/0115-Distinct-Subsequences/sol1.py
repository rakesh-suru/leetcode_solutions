class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        ans = 0

        def solve(idx, curr):
            nonlocal ans

            if idx == n:
                if curr == t:
                    ans += 1
                return
            
            solve(idx + 1, curr + s[idx])
            solve(idx + 1, curr)
        
        solve(0, "")
        return ans
            
