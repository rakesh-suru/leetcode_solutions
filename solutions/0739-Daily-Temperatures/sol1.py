class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n - 1):
            for j in range(i + 1, n):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break
        return ans