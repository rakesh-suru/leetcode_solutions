class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)

        ans = 0

        for ch in chars:
            if ch.islower() and ch.upper() in chars:
                ans += 1

        return ans