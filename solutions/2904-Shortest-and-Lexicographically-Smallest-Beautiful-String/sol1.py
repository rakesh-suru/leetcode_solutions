class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        left = 0
        cnt = 0

        for right in range(n):
            if s[right] == "1":
                cnt += 1

            while cnt > k:
                if s[left] == "1":
                    cnt -= 1
                left += 1

            if cnt == k:
                while s[left] == "0":
                    left += 1

                curr = s[left:right + 1]

                if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                    ans = curr

        return ans