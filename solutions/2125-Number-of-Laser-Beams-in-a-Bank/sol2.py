class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        temp = [row.count("1") for row in bank]

        for i in range(len(temp) - 1):
            if temp[i] == 0:
                continue
            j = i + 1
            while j < len(temp) and temp[j] == 0:
                j += 1
            if j < len(temp):
                ans += temp[i] * temp[j]
        return ans
