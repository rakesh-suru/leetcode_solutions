class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        @lru_cache(None)
        def dfs(i, j):
            if i == n or j == m:
                return float('-inf')

            curr = nums1[i] * nums2[j]

            return max(
                curr,
                curr + dfs(i+1, j+1),
                dfs(i+1, j),
                dfs(i, j+1)
            )

        return dfs(0, 0)
