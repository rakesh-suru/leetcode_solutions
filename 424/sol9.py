class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, maxf, maxlen = 0, 0, 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            maxf = max(maxf, count[idx])

            if (r - l + 1) - maxf > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen
