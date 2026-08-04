class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        ans = [''] * len(s)
        l, r = 0, len(s) - 1

        for i in range(26):
            while freq[i] >= 2:
                ans[l] = chr(i + 97)
                ans[r] = chr(i + 97)
                l += 1
                r -= 1
                freq[i] -= 2

        for i in range(26):
            if freq[i]:
                ans[l] = chr(i + 97)
                break

        return "".join(ans)