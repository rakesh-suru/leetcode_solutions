class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ans = set()
        n = len(s)

        def solve(idx, temp):
            if idx == n:
                if temp:
                    ans.add(temp)
                return
            
            solve(idx + 1, temp + s[idx])
            solve(idx + 1, temp)
        
        solve(0, "")
        return len(ans)