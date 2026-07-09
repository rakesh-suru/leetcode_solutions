class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapper = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = []
        path = []

        def solve(idx):

            if idx == len(digits):
                ans.append("".join(path))
                return

            for ch in mapper[digits[idx]]:
                path.append(ch)
                solve(idx+1)
                path.pop()

        solve(0)
        return ans