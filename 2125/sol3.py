class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp = []
        ans = 0
        for i in bank:
            if i.count("1") != 0:
                temp.append(i.count("1"))
        for i in range(len(temp)-1):
            ans += temp[i] * temp[i+1]
        return ans