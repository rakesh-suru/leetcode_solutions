class Solution:
    def countAsterisks(self, s: str) -> int:
        idx = [i for i, ch in enumerate(s) if ch == "|"]

        if len(idx) == 0:
            return s.count("*")

        ans = 0
        ans += s[:idx[0]].count("*")
        ans += s[idx[-1] + 1:].count("*")

        for i in range(1, len(idx) - 1, 2):
            ans += s[idx[i] + 1:idx[i + 1]].count("*")

        return ans