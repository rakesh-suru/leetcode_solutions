class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def dfs(num, last):
            if low <= num <= high:
                ans.append(num)

            if num > high or last == 9:
                return

            dfs(num * 10 + last + 1, last + 1)

        for i in range(1, 10):
            dfs(i, i)

        ans.sort()
        return ans