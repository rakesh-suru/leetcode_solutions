class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0
        s_one = float('inf')
        s_two = float('inf')

        for n in nums:
            ans += n
            if n % 3 == 1:
                s_two = min(s_two, n + s_one)
                s_one = min(s_one, n)
            if n % 3 == 2:
                s_one = min(s_one, n + s_two)
                s_two = min(s_two, n)
        
        if ans % 3 == 0:
            return ans
        if ans % 3 == 1:
            return ans - s_one
        if ans % 3 == 2:
            return ans - s_two
