class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp = [row.count("1") for row in bank if "1" in row]
        ans = 0
        for i in range(len(temp)-1):
            ans += temp[i] * temp[i+1]
        return ans