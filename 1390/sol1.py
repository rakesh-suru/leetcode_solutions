class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        divs = []
        for num in nums:
            temp = []
            for i in range(1, num//2 + 1):
                if num % i == 0:
                    temp.append(i)
            temp.append(num)
            if len(temp) == 4:
                divs.append(temp)
            temp = []
        
        if not divs:
            return 0
        for div in divs:
            ans += sum(div)
        
        return ans