class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                ch = c.lower()
                if ch not in first_upper:
                    first_upper[ch] = i

        ans = 0

        for ch in last_lower:
            if ch in first_upper:
                if last_lower[ch] < first_upper[ch]:
                    ans += 1

        return ans