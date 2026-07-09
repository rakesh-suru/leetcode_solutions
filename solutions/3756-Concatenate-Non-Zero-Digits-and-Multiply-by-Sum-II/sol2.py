class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        prefix = [0]
        for ch in s:
            prefix.append(prefix[-1] + int(ch))

        ans = []

        for l, r in queries:
            digit_sum = prefix[r + 1] - prefix[l]

            num = 0
            for i in range(l, r + 1):
                if s[i] != '0':
                    num = (num * 10 + int(s[i])) % MOD

            ans.append((num * digit_sum) % MOD)

        return ans