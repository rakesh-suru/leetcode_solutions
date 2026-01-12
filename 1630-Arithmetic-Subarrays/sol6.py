class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkValid(arr: List[int]) -> bool:
            n = len(arr)
            if n <= 2: return True
            arr.sort()
            expected_sum = n * (arr[0] + arr[-1]) // 2
            return sum(arr) == expected_sum and all(arr[i]-arr[i-1]==arr[1]-arr[0] for i in range(2,n))
        
        return [checkValid(nums[l[i]:r[i]+1]) for i in range(len(l))]
