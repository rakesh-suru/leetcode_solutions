class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkValid(arr: List[int]) -> bool:
            n = len(arr)
            if n < 2: return True
            min_val, max_val = min(arr), max(arr)
            if (max_val - min_val) % (n-1) != 0:
                return False
            d = (max_val - min_val) // (n-1)
            if d == 0:
                return len(set(arr)) == 1
            expected = {min_val + i*d for i in range(n)}
            return set(arr) == expected

        ans = []
        for i in range(len(l)):
            ans.append(checkValid(nums[l[i] : r[i] + 1]))
        return ans
