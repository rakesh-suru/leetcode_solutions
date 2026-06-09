class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = n, m
        lcs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        lcs.reverse()

        i = j = 0
        ans = []

        for ch in lcs:

            while i < n and str1[i] != ch:
                ans.append(str1[i])
                i += 1

            while j < m and str2[j] != ch:
                ans.append(str2[j])
                j += 1

            ans.append(ch)
            i += 1
            j += 1

        while i < n:
            ans.append(str1[i])
            i += 1

        while j < m:
            ans.append(str2[j])
            j += 1

        return "".join(ans)