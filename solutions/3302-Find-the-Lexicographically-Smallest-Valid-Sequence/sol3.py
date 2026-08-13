class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        from functools import lru_cache

        m = len(word1)
        n = len(word2)

        @lru_cache(None)
        def solve(i, j, used):
            if j == n:
                return True

            if i == m:
                return False

            if m - i < n - j:
                return False

            if word1[i] == word2[j]:
                if solve(i + 1, j + 1, used):
                    return True

            if not used:
                if solve(i + 1, j + 1, True):
                    return True

            if solve(i + 1, j, used):
                return True

            return False

        if not solve(0, 0, False):
            return []

        ans = []
        i = 0
        j = 0
        used = False

        while j < n:
            while i < m:

                if word1[i] == word2[j]:
                    if solve(i + 1, j + 1, used):
                        ans.append(i)
                        i += 1
                        j += 1
                        break

                if not used:
                    if solve(i + 1, j + 1, True):
                        ans.append(i)
                        i += 1
                        j += 1
                        used = True
                        break
                i += 1

        return ans