class Solution:
    def countHillValley(self, temp: List[int]) -> int:
        nums = [temp[0]]
        for i in range(1,len(temp)):
            if temp[i-1] != temp[i]:
                nums.append(temp[i])
        ans = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                ans += 1
            elif nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                ans += 1
        return ans