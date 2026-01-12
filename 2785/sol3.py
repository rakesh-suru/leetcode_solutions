class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        temp = []
        ans = ""
        
        for ch in s:
            if ch in vowels:
                ans += "-"
                temp.append(ch)
            else:
                ans += ch
        
        temp.sort()

        result = ""
        cnt = 0
        for ch in ans:
            if ch == "-":
                result += temp[cnt]
                cnt += 1
            else:
                result += ch
        
        return result
