class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        i = s.find('6')
        return int(s if i == -1 else s[:i] + '9' + s[i+1:])
