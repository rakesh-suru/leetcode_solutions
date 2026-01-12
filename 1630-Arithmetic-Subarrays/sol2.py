class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def checkValid(temp: List[int]):
            temp.sort()
            for i in range(len(temp)-2):
                if temp[i] - temp[i+1] != temp[i+1] - temp[i+2]:
                    return False
            return True

        ans = []
        for i in range(len(l)):
            ans.append(checkValid(nums[l[i] : r[i] + 1]))
        
        return ans
        