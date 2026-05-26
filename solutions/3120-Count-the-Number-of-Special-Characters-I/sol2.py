class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        ans = 0
        visited = set()

        for ch in word:
            if ch.islower() and ch not in visited:
                if ch.upper() in word:
                    visited.add(ch)
                    ans += 1

        return ans