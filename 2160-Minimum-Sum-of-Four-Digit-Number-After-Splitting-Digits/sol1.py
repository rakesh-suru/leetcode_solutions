class Solution:
    def minimumSum(self, num: int) -> int:
        temp = [int(i) for i in str(num)]
        temp.sort()
        num1 = temp[0] * 10 + temp[3]
        num2 = temp[1] * 10 + temp[2]

        return num1 + num2