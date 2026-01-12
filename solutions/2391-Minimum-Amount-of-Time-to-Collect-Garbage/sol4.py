class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        last = {'G': 0, 'P': 0, 'M': 0}

        for i, s in enumerate(garbage):
            total_time += len(s)
            for c in s:
                last[c] = i

        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]

        for c in 'GPM':
            if last[c] > 0:
                total_time += travel[last[c] - 1]

        return total_time
