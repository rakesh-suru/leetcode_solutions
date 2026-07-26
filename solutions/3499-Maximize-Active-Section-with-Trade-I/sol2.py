class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        groups = []

        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            groups.append((s[i], j - i))
            i = j

        ans = ones

        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                gain = groups[i - 1][1] + groups[i + 1][1]
                ans = max(ans, ones + gain)

        return ans