class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {"2" : "abc",
                "3" : "def",
                "4" : "ghi",
                "5" : "jkl",
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz"}
        
        n = len(digits)
        ans = []

        def solve(idx, temp):
            if idx == n:
                ans.append(temp)
                return
            
            for char in mapper[digits[idx]]:
                solve(idx + 1, temp + char)
        
        solve(0, "")
        return ans