class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        for ch in word:
            if not ch.isalnum():
                return False

        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0

        for ch in word:
            if ch.isalpha():
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

        return vowel_count > 0 and consonant_count > 0
