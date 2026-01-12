class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = 0
        total = n * (n + 1) // 2
        for i in range(1, n + 1):
            prefix_sum += i
            if prefix_sum == total - prefix_sum + i:
                return i
        return -1
