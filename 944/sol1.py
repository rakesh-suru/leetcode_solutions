class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            if strs != sorted(strs, key = lambda x : x[i]):
                ans += 1
        return ans