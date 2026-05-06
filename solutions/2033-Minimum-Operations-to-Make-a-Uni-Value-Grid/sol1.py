class Solution:
    def minOperations(self, grid: List[List[int]], x: int):
        temp = []

        for row in grid:
            for val in row:
                temp.append(val)

        temp.sort()

        rem = temp[0] % x
        for num in temp:
            if num % x != rem:
                return -1

        mid = temp[len(temp) // 2]

        ans = 0
        for num in temp:
            ans += abs(mid - num) // x

        return ans