class Solution:
    def checkValidString(self, s: str) -> bool:
        ans = False
        n = len(s)

        def solve(idx, cnt):
            nonlocal ans
            if idx == n:
                if cnt == 0:
                    ans = True
                return
            
            if s[idx] == "(":
                return solve(idx + 1, cnt + 1)
            elif s[idx] == ")":
                return solve(idx + 1, cnt - 1)
            else:
                return solve(idx + 1, cnt) or solve(idx + 1, cnt - 1) or solve(idx + 1, cnt + 1)
        
        solve(0, 0)
        return ans