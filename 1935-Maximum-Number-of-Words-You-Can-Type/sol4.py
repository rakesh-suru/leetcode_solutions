class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        ans = 0
        for word in text.split():
            if not (set(word) & broken):
                ans += 1
        return ans
