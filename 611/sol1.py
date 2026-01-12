class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b > c and b + c > a and a + c > b:
                        ans += 1
        return ans