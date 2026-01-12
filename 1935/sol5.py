class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for word in text.split():
            w = word
            for ch in brokenLetters:
                w = w.replace(ch, "*")
            if w == word:
                ans += 1
        return ans
