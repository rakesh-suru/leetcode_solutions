class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        it = iter(sorted(ch for ch in s if ch in vowels))
        return "".join(next(it) if ch in vowels else ch for ch in s)
