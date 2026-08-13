class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)

        from functools import lru_cache

        @lru_cache(None)
        def solve(i, j, used):
            if j == n:
                return ()

            if i == m:
                return None

            best = None

            res = solve(i + 1, j, used)

            if res is not None:
                best = res

            if word1[i] == word2[j]:
                res = solve(i + 1, j + 1, used)

                if res is not None:
                    candidate = (i,) + res

                    if best is None or candidate < best:
                        best = candidate

            elif not used:
                res = solve(i + 1, j + 1, True)

                if res is not None:
                    candidate = (i,) + res

                    if best is None or candidate < best:
                        best = candidate

            return best

        ans = solve(0, 0, False)

        return list(ans) if ans is not None else []