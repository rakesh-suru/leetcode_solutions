class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7
        ans = 0

        for i in range(n):
            temp_min = arr[i]
            for j in range(i, n):
                temp_min = min(temp_min, arr[j])
                ans += temp_min

        return ans % mod