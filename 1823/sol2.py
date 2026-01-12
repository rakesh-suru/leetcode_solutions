class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp = [i + 1 for i in range(n)]
        curr = 0

        while len(temp) > 1:
            curr = (curr + k - 1) % len(temp)
            temp = temp[:curr] + temp[curr+1:]

        return temp[0]
