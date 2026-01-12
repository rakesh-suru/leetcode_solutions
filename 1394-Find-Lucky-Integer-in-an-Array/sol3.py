class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for num in sorted(arr):
            if num == arr.count(num) and num > ans:
                ans = num

        return ans