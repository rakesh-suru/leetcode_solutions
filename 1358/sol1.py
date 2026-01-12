class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        lastseen = [-1, -1, -1]
        for i in range(len(s)):
            lastseen[ord(s[i]) - 97] = i
            if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:
                ans += min(lastseen) + 1
        return ans