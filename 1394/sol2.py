class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        cnt = Counter(arr)
        for num in cnt:
            if num == cnt[num] and num > ans:
                ans = num

        return ans