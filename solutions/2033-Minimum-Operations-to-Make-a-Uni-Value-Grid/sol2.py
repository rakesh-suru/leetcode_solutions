class Solution:
    def minOperations(self, grid, x):
        arr = [num for row in grid for num in row]

        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1


        def quickselect(nums, k):
            pivot = random.choice(nums)
            left = [n for n in nums if n < pivot]
            mid = [n for n in nums if n == pivot]
            right = [n for n in nums if n > pivot]

            if k < len(left):
                return quickselect(left, k)
            elif k < len(left) + len(mid):
                return pivot
            else:
                return quickselect(right, k - len(left) - len(mid))

        median = quickselect(arr, len(arr) // 2)

        return sum(abs(num - median) // x for num in arr)