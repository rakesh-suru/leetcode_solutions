class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        
        result = ""
        
        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)
            
            index = k // fact
            result += nums[index]
            
            nums.pop(index)
            k %= fact
        
        return result
