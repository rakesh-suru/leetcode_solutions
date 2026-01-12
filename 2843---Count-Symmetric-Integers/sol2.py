class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            temp = str(num)
            if len(temp) % 2 == 0:
                half = len(temp) // 2
                s1 = sum(int(i) for i in temp[:half])
                s2 = sum(int(i) for i in temp[half:])
                if s1 == s2:
                    ans += 1
        return ans
