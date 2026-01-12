class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high+1):
            temp = str(num)
            if len(temp) % 2 != 0:
                continue
            templen = len(temp)//2
            s1 = sum(int(i) for i in temp[:templen])
            s2 = sum(int(i) for i in temp[templen:])
            if s1 == s2:
                ans += 1
        return ans