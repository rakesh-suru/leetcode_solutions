class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mapper = Counter(s)
        count = mapper[s[0]]

        for key in mapper:
            if mapper[key] != count:
                return False
        
        return True