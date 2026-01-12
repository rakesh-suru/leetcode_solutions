class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2*i)+1 for i in range(n)]
        left = 0
        right = n-1
        ans = 0
        while left < right:
            while arr[left] < arr[right]:
                arr[left] += 1
                arr[right] -= 1
                ans += 1
            left += 1
            right -= 1
        return ans