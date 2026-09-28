class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = 0
        n = len(s)

        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                temp = s[i : i + 2]
                i += 3
            else:
                temp = s[i]
                i += 1
            
            ans += chr(int(temp) - 1 + ord("a"))
        
        return ans