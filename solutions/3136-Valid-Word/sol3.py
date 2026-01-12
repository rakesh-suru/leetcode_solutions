class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not all(ch.isalnum() for ch in word):
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = any(ch in vowels for ch in word if ch.isalpha())
        has_consonant = any(ch.isalpha() and ch not in vowels for ch in word)

        return has_vowel and has_consonant
