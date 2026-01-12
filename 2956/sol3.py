class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        set1, set2 = set(nums1), set(nums2)

        ans1 = sum(count1[num] for num in set1 if num in set2)
        ans2 = sum(count2[num] for num in set2 if num in set1)
        return [ans1, ans2]
