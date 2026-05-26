class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        '''
        mapper = defaultdict()
        for i in range(26):
            mapper[chr((ord("a") + i))] = chr((ord("A") + i))
        '''
        
        ans = 0
        visited = set()

        for char in word:
            temp = ord(char)

            if ord("a") <= temp <= ord("z") and char not in visited:
                upper = chr(temp - ord("a") + ord("A"))

                if upper in word:
                    visited.add(char)
                    ans += 1

        return ans