class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0

        for i, ch in enumerate(s):
            if (int(ch) ^ (i % 2)) == 1:
                cnt += 1

        return min(cnt, len(s) - cnt)