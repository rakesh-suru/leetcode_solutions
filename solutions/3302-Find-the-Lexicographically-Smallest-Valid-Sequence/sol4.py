class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)

        suf = [-1] * n

        i = m - 1

        for j in range(n - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suf[j] = i
            i -= 1

        ans = []
        i = 0
        j = 0
        used = False

        while i < m and j < n:

            if word1[i] == word2[j]:
                ans.append(i)
                i += 1
                j += 1
                continue

            if not used:
                if j == n - 1 or (suf[j + 1] != -1 and suf[j + 1] > i):
                    ans.append(i)
                    used = True
                    i += 1
                    j += 1
                    continue

            i += 1

        return ans if j == n else []