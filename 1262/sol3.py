class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        if total % 3 == 0:
            return total
        
        rem = total % 3
        
        nums1 = sorted([x for x in nums if x % 3 == 1])
        nums2 = sorted([x for x in nums if x % 3 == 2])
        
        if rem == 1:
            cand = []
            if nums1:
                cand.append(total - nums1[0])
            if len(nums2) >= 2:
                cand.append(total - nums2[0] - nums2[1])
            return max(cand) if cand else 0
        
        if rem == 2:
            cand = []
            if nums2:
                cand.append(total - nums2[0])
            if len(nums1) >= 2:
                cand.append(total - nums1[0] - nums1[1])
            return max(cand) if cand else 0
