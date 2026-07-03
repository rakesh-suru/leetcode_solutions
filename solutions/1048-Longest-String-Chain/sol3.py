class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)

        dp = [1] * n
        ans = 1

        def check(a, b):
            if len(b) != len(a) + 1:
                return False

            i = j = 0

            while j < len(b):
                if i < len(a) and a[i] == b[j]:
                    i += 1
                j += 1

            return i == len(a)

        for i in range(n):
            for j in range(i):
                if check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

            ans = max(ans, dp[i])

        return ans