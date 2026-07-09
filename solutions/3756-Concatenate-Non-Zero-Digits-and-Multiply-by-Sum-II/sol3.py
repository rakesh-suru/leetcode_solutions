class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        ans = []

        for l, r in queries:
            sub = s[l:r+1]

            digit_sum = sum(int(ch) for ch in sub)

            num = 0
            for ch in sub:
                if ch != '0':
                    num = (num * 10 + int(ch)) % MOD

            ans.append((num * digit_sum) % MOD)

        return ans