class Solution:
    def minOperations(self, s: str) -> int:
        zero = ""
        one = ""

        for i in range(len(s)):
            if i % 2:
                zero += "0"
                one += "1"
            else:
                zero += "1"
                one += "0"
        
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            if s[i] != zero[i]:
                cnt1 += 1
            if s[i] != one[i]:
                cnt2 += 1
        
        return min(cnt1, cnt2)