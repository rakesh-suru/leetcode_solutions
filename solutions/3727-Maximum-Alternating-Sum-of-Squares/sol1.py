class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        temp = [abs(x) for x in nums]
        temp.sort(reverse = True)

        ans = 0
        n = len(nums)
        if n % 2 == 0:
            for i in range(n//2):
                ans += temp[i] * temp[i]
            for i in range(n//2, n):
                ans -= temp[i] * temp[i]
        
        else:
            for i in range(n//2 + 1):
                ans += temp[i] * temp[i]
            for i in range(n//2 + 1, n):
                ans -= temp[i] * temp[i]
        
        return ans
