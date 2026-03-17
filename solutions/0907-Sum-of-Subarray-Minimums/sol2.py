class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7

        stack = []
        left = [0] * n
        right = [0] * n

        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))

        stack = []

        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        ans = 0
        for i in range(n):
            ans += arr[i] * left[i] * right[i]

        return ans % mod