class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        n = original
        k = 0
        leng = len(nums)
        while k<leng:
            if nums[k]==n:
                n*=2
            k+=1
        return n