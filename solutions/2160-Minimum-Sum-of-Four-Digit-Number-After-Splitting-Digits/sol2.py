class Solution:
    def minimumSum(self, num: int) -> int:
        temp = [int(i) for i in str(num)]
        temp.sort()

        return temp[0] * 10 + temp[3] + temp[1] * 10 + temp[2]