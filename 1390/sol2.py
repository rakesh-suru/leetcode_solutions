class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            divs = []
            for i in range(1, num//2 + 1):
                if num % i == 0:
                    divs.append(i)
                if len(divs) > 3:
                    break
            divs.append(num)
            if len(divs) == 4:
                ans += sum(divs)
        return ans
