class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        temp = nums[0]
        ans = [False if temp else True]
        for i in range(1,len(nums)):
            temp = temp * 2 + nums[i]
            if temp % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
