class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        temp = list(s)
        i = 0
        n = len(temp)

        while i < n // 2:
            if temp[i] == temp[n - i - 1]:
                i += 1
            elif temp[i] < temp[n - i - 1]:
                temp[n - i - 1] = temp[i]
            else:
                temp[i] = temp[n - i - 1]
        
        return "".join(temp)
                