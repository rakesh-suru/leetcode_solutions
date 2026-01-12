class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s1 , t1 = {}, {}
        l = len(s)
        ans = 0
        for i in range(l):
            s1[s[i]] = i
            t1[t[i]] = i
        
        for char, index in s1.items():
            ans += abs(index - t1[char])
        
        return ans