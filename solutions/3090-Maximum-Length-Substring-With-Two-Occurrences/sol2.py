class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        right = 0
        n = len(s)
        cnt = defaultdict(int)

        while right < n:
            cnt[s[right]] += 1

            while cnt[s[right]] > 2:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans