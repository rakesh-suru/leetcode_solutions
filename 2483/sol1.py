class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = float('inf')
        best = -1
        n = len(customers)

        for i in range(n + 1):
            temp = 0

            for j in range(i):
                if customers[j] == "N":
                    temp += 1

            for k in range(i, n):
                if customers[k] == "Y":
                    temp += 1

            if temp < ans:
                ans = temp
                best = i

        return best
