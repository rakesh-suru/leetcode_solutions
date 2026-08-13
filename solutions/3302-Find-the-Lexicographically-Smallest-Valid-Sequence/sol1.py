class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)

        self.ans = None

        def solve(i, j, idx, used):
            if j == n:
                if self.ans is None or idx < self.ans:
                    self.ans = idx
                return

            if i == m:
                return

            if word1[i] == word2[j]:
                solve(i + 1, j + 1, idx + [i], used)

            if not used and word1[i] != word2[j]:
                solve(i + 1, j + 1, idx + [i], True)

            solve(i + 1, j, idx, used)

        solve(0, 0, [], False)

        return self.ans if self.ans is not None else []