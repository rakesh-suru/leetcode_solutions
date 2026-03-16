class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        temp = nums + nums
        length = len(nums)
        nge = [-1] * length

        for i in range(length):
            for j in range(i + 1, i + length):
                if nums[i] < temp[j]:
                    nge[i] = temp[j]
                    break
        return nge