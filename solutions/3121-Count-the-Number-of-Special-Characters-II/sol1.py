class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapper = defaultdict()
        ans = 0

        for i, c in enumerate(word):
            if c.isupper() and c in mapper:
                continue
            mapper[c] = i
        
        for char in mapper:
            if char.islower() and char.upper() in mapper:
                if mapper[char] < mapper[char.upper()]:
                    ans += 1
        return ans
            