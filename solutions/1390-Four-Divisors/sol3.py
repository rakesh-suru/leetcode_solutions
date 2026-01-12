class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            divs = set()
            i = 1
            while i * i <= num:
                if num % i == 0:
                    divs.add(i)
                    divs.add(num // i)
                    if len(divs) > 4:
                        break
                i += 1

            if len(divs) == 4:
                ans += sum(divs)

        return ans
