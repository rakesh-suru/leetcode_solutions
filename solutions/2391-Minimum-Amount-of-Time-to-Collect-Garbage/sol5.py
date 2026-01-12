class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        last_g = last_p = last_m = 0
        prefix = 0

        for i in range(len(garbage)):
            total_time += len(garbage[i])

            if 'G' in garbage[i]:
                last_g = prefix
            if 'P' in garbage[i]:
                last_p = prefix
            if 'M' in garbage[i]:
                last_m = prefix

            if i < len(travel):
                prefix += travel[i]

        total_time += last_g + last_p + last_m
        return total_time
