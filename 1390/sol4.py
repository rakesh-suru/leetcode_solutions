class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            count = 0
            total = 0
            i = 1

            while i * i <= num:
                if num % i == 0:
                    j = num // i
                    count += 1
                    total += i
                    if i != j:
                        count += 1
                        total += j
                if count > 4:
                    break
                i += 1

            if count == 4:
                ans += total

        return ans
