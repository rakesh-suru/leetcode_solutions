class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 0:
            return []

        nums.sort()

        dp = [1] * n
        parent = list(range(n))

        max_len = 1
        last_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                last_idx = i

        ans = []

        while parent[last_idx] != last_idx:
            ans.append(nums[last_idx])
            last_idx = parent[last_idx]

        ans.append(nums[last_idx])

        return ans[::-1]