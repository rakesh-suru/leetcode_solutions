class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        ans = ones
        prevZero = None

        i = 0

        while i < len(s):

            j = i

            while j < len(s) and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '0':
                if prevZero is not None:
                    ans = max(ans, ones + prevZero + length)
                prevZero = length

            i = j

        return ans