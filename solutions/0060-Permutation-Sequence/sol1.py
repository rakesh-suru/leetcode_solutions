class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        for i in range(1 , n + 1):
            nums.append(str(i))
        
        temp = k - 1
        ans = ""
        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)

            q = temp // fact
            ans += nums[q]
            nums.remove(nums[q])
            temp = temp % fact
        
        return ans