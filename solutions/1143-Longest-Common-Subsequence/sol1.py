class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ans = []

        def backtrack(idx, curr, n, text):
            if idx == n:
                ans.append(curr)
                return

            backtrack(idx + 1, curr + text[idx], n, text)
            backtrack(idx + 1, curr, n, text)

        backtrack(0, "", len(text1), text1)
        backtrack(0, "", len(text2), text2)

        subseq1 = ans[: 2 ** len(text1)]
        subseq2 = set(ans[2 ** len(text1) :])

        ans = 0

        for word in subseq1:
            if word in subseq2:
                ans = max(ans, len(word))
        return ans

