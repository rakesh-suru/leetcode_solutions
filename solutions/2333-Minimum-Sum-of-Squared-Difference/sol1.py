class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        ans = 0
        k = k1 + k2
        arr = []
        n = len(nums1)

        for i in range(n):
            temp = abs(nums1[i] - nums2[i])
            arr.append(temp)
        
        arr.sort()

        while k > 0:
            if arr[-1] <= 0:
                break
            arr[-1] -= 1
            arr.sort()
            k -= 1
        
        for num in arr:
            ans += num * num
        
        return ans