from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)

        for right in range(len(s)):
            cnt[s[right]] += 1

            while cnt[s[right]] > 2:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans