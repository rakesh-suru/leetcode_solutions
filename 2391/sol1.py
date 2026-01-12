class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0

        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]

        for i in range(len(garbage) - 1, -1, -1):
            if 'G' in garbage[i]:
                ans += sum(g.count('G') for g in garbage[:i + 1])
                ans += travel[i - 1] if i > 0 else 0
                break

        for i in range(len(garbage) - 1, -1, -1):
            if 'P' in garbage[i]:
                ans += sum(g.count('P') for g in garbage[:i + 1])
                ans += travel[i - 1] if i > 0 else 0
                break

        for i in range(len(garbage) - 1, -1, -1):
            if 'M' in garbage[i]:
                ans += sum(g.count('M') for g in garbage[:i + 1])
                ans += travel[i - 1] if i > 0 else 0
                break

        return ans
