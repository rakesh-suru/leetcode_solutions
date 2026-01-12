class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        temp = []
        ans = []
        for i in range(len(s)):
            if s[i] not in vowels:
                ans.append(s[i])
            else:
                ans.append("-")
                temp.append(s[i])
        
        temp.sort()
        cnt = 0
        for i in range(len(ans)):
            if ans[i] == "-":
                ans[i] = temp[cnt]
                cnt += 1
        
        return "".join(ans)

        