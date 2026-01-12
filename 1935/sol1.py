class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        ans = len(words)
        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    ans -= 1
                    break
        return ans