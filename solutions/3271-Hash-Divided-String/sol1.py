class Solution:
    def stringHash(self, s: str, k: int) -> str:
        mapping = dict()
        for i in range(26):
            mapping[chr(ord("a") + i)] = i
        
        result = ""
        for x in range(len(s)//k):
            temp = s[x * k : (x+1) * k]
            ans = 0
            for char in temp:
                ans += mapping[char]
            ans = ans % 26
            for val in mapping:
                if mapping[val] == ans:
                    result += val
        return result