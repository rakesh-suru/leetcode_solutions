class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_cnt = -1
        zero_cnt = 0
        for i in s:
            if i == "1":
                one_cnt += 1
            else:
                zero_cnt += 1
        return "1"*one_cnt + "0"*zero_cnt + "1" 