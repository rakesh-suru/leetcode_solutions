class Solution:

    def pse(self, arr):
        n = len(arr)
        stack = []
        res = [-1] * n

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1]
            
            stack.append(i)

        return res

    def nse(self, arr):
        n = len(arr)
        stack = []
        res = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1]
            
            stack.append(i)

        return res

    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)

        left = self.pse(arr)
        right = self.nse(arr)

        ans = 0

        for i in range(n):
            left_count = i - left[i]
            right_count = right[i] - i

            ans += arr[i] * left_count * right_count

        return ans % mod