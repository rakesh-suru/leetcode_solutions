class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        ans = False
        n = len(s)
        
        def solve(idx):
            nonlocal ans

            if idx == n - 1:
                ans = True
                return
            
            if idx < 0 or idx >= n:
                return
            
            left = min(idx + minJump, n - 1)
            right = min(idx + maxJump, n - 1)
            

            for i in range(left, right + 1):
                if s[i] == "0":
                    solve(i)
        
        solve(0)
        return ans