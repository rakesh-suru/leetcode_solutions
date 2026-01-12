class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkValid(arr: List[int]) -> bool:
            arr.sort()
            d = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != d:
                    return False
            return True

        return [checkValid(nums[l[i]:r[i]+1]) for i in range(len(l))]
