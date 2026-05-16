class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        for num in range(num1, num2 + 1):
            temp = str(num)
            cnt = 0

            if len(temp) < 3:
                continue
            
            for i in range(1, len(temp) - 1):
                if int(temp[i-1]) < int(temp[i]) > int(temp[i + 1]):
                    cnt += 1
                elif int(temp[i-1]) > int(temp[i]) < int(temp[i + 1]):
                    cnt += 1
            
            ans += cnt
        return ans