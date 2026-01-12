class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        l = 0
        while l + 2 < len(num):
            if num[l] == num[l+1] == num[l+2]:
                ans = max(ans, num[l:l+3])
            l += 1
        return ans
