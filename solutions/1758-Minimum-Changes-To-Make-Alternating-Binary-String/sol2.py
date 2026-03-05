class Solution:
    def minOperations(self, s: str) -> int:
        mismatch1 = 0
        mismatch2 = 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                mismatch1 += 1
            if s[i] != str((i + 1) % 2):
                mismatch2 += 1

        return min(mismatch1, mismatch2)