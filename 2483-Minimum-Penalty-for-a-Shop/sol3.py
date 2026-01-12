class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        prefixN = [0] * (n + 1)
        suffixY = [0] * (n + 1)

        for i in range(n):
            prefixN[i + 1] = prefixN[i] + (customers[i] == 'N')

        for i in range(n - 1, -1, -1):
            suffixY[i] = suffixY[i + 1] + (customers[i] == 'Y')

        ans = float('inf')
        best = 0

        for i in range(n + 1):
            penalty = prefixN[i] + suffixY[i]
            if penalty < ans:
                ans = penalty
                best = i

        return best
