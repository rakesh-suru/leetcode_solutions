def min_sum(nums):
            n = len(nums)
            stack = []
            res = 0
            
            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] > nums[i]):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    right = i
                    
                    count = (mid - left) * (right - mid)
                    res += nums[mid] * count
                
                stack.append(i)
            
            return res
        
        
        def max_sum(nums):
            n = len(nums)
            stack = []
            res = 0
            
            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] < nums[i]):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    right = i
                    
                    count = (mid - left) * (right - mid)
                    res += nums[mid] * count
                
                stack.append(i)
            
            return res
        
        
        return max_sum(nums) - min_sum(nums)