class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        self.ans = False
        l = len(s1)

        def solve(temp, idx):
            if temp == s2:
                self.ans = True
                return
            
            if idx == l or self.ans:
                return
            
            for i in range(idx, l, 2):
                new_temp = temp[:idx] + temp[i] + temp[idx + 1:i] + temp[idx] + temp[i + 1:]
                solve(new_temp, idx + 1)

        solve(s1, 0)
        return self.ans