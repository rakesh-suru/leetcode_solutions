class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = [i for i in str(num)]
        for i in range(len(temp)):
            if temp[i] == '6':
                temp[i] = '9'
                break
        return int(''.join(temp))