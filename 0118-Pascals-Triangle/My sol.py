class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            temp = []
            num = 11 ** i
            cha = str(num)
            for j in cha:
                temp.append(int(j))
            ans.append(temp)
        return ans