class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        last_g = last_p = last_m = 0

        for i in range(len(garbage)):
            ans += len(garbage[i])
            if "G" in garbage[i]:
                last_g = i
            if "P" in garbage[i]:
                last_p = i
            if "M" in garbage[i]:
                last_m = i

        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
            
        if last_g >0:
            ans += travel[last_g - 1]
        if last_p >0:
            ans += travel[last_p - 1]
        if last_m >0:
            ans += travel[last_m - 1]
            
        return ans
