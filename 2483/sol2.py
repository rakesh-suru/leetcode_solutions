class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = float('inf')
        best = -1
        n = len(customers)

        for i in range(n + 1):
            no = customers[0:i].count("N")
            yes = customers[i:n].count("Y")

            if no + yes < ans:
                ans = no + yes
                best = i

        return best
