class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            left = mid * (mid + 1) // 2
            right = total - (mid - 1) * mid // 2
            if left == right:
                return mid
            elif left < right:
                low = mid + 1
            else:
                high = mid - 1
        return -1
