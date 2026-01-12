class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp = dict()
        for edge in edges:
            for i in edge:
                if i not in temp:
                    temp[i] = 1
                else:
                    temp[i] += 1
        ans = 0
        for i in temp:
            if temp[i] == len(temp) - 1:
                return i
        return None